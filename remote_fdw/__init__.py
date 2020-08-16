import codecs
import csv
from urllib import request

from multicorn import ForeignDataWrapper
from multicorn.utils import log_to_postgres
from logging import WARNING

class RemoteCsvFDW(ForeignDataWrapper):
    def __init__(self, fdw_options, fdw_columns):
        super(RemoteCsvFDW, self).__init__(fdw_options, fdw_columns)
        self.filename = fdw_options["filename"]
        self.delimiter = fdw_options.get("delimiter", ",")
        self.header = fdw_options.get('header', True)
        self.columns = fdw_columns

    def execute(self, quals, columns):
        with request.urlopen(self.filename) as stream:
            reader = csv.reader(codecs.iterdecode(stream, 'utf-8'), delimiter=self.delimiter)
            count = 0
            checked = False
            for line in reader:
                if not self.header or self.header and count>=1:
                    if not checked:
                        # On first iteration, check if the lines are of the
                        # appropriate length
                        checked = True
                        if len(line) > len(self.columns):
                            log_to_postgres("There are more columns than "
                                            "defined in the table", WARNING)
                        if len(line) < len(self.columns):
                            log_to_postgres("There are less columns than "
                                            "defined in the table", WARNING)
                    yield line[:len(self.columns)]
                count += 1