# baseball-data-analysis
Playground for performing simple analysis on open-source baseball data 2010-2017

## Dependencies
* Virtual env manages all Python 3.5 package dependencies
* Postgresql: https://www.postgresql.org/download/

## How to Use
1) Run start_db.sh from the directory you want to save the Postgres DB in
2) Run the setup python script
```venv/python setup.py```

docker run -d -p 5432:5432 postgres-server