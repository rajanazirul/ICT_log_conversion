# Convert ICT parameter to json or insert directly to SQL.

## 1. Overview
What we'll be doing
1. Convert diagnostic log 
2. Convert probe log
3. Convert test log from production


## 2. Getting Started
git clone `https://github.com/rajanazirul/ict_log_conversion.git`

`cd ict_log_conversion`

Setup virtual environment

`virtualenv env -p python3`

for windows, copy path `\env\Scripts\activate.bat`

open terminal and paste the path. If success will show (env) at the terminal

test run the script

```
python extract_paramDGN.py
python extract_paramJSON.py
python extract_paramProbe.py
```

## 3. Setup Database using PostgreSQL
install pgadmin with postgresql on link `https://www.postgresql.org/download/`

add PATH `C/postgresql12/Bin` to windows environment

create user for postgresql

Start menu > All Programs > PostgreSQL 8.3 > psql to 'postgres'.

This opens up the psql interactive terminal.
`CREATE ROLE username LOGIN PASSWORD 'password' NOINHERIT CREATEDB;`

create database by using following command on psql
`createdb ict_demo`

open create_table_dgn.py, create_table_probe.py, create_table_ictjson.py file

config the host, dbname, user, password, then run the script

```
python create_table_dgn.py
python create_table_ictjson.py
python create_table_probe.py
```

open PGadmin to check database or use psql terminal by command `\c userlist`



