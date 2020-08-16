# Remote csv fdw
install Multicorn:
using pgxn: 
```buildoutcfg
    sudo pgxn install multicorn
```
or using apt on Debian (actual versions: https://launchpad.net/ubuntu/+source/postgresql-multicorn):
```buildoutcfg
    sudo apt install postgresql-12-python3-multicorn
```
reuirements: 
```buildoutcfg
    sudo apt-get install build-essential postgresql-server-dev-12 python3-dev python3-setuptools python3-pip postgresql-plpython3-12

```
install package:
```buildoutcfg    
    git clone https://github.com/Khakov/remote_csv_fdw.git
    cd remote_csv_fdw
    python setup.py install
    
```


create foreign server:
```
CREATE SERVER remote_csv_fdw FOREIGN DATA WRAPPER multicorn OPTIONS (
    WRAPPER 'csvgz_fdw.CSVGZForeignDataWrapper'
);
```

```
CREATE FOREIGN TABLE FDW_TEST (
    A INTEGER,
    B VARCHAR,
    C TEXT,
    D TEXT,
    E TIMESTAMP
) SERVER CSVGZ_SRV OPTIONS (
    FILE_NAME '/opt/PostgreSQL/csv/test.csv.gz'
);
CREATE FOREIGN TABLE FDW_TEST2 (
    A INTEGER,
    B VARCHAR,
    C TEXT,
    D TEXT,
    E TIMESTAMP
) SERVER CSVGZ_SRV OPTIONS (
    FILE_NAME '/opt/PostgreSQL/csv/test.csv'
);
```