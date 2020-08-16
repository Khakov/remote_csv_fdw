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
create extension multicorn;
CREATE SERVER remote_csv_fdw FOREIGN DATA WRAPPER multicorn OPTIONS (
    WRAPPER 'remote_fdw.RemoteCsvFDW'
);
```

```
CREATE FOREIGN TABLE test (
    Username varchar,
    Identifier int,
    "First name" varchar,
    "Last name" varchar
) SERVER remote_csv_fdw OPTIONS (
    file_name 'https://support.staffbase.com/hc/en-us/article_attachments/360009197031/username.csv'
);
```