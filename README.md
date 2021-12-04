# oc_projet_p8

Créez une plateforme pour amateurs de Nutella

## About that Readme

Develop into branch develop. Thank to change if you want to see the progress work

## How to build and run the HTTP server

### Clone the repo

`$ git clone: https://github.com/SergueiNK/oc_projet_p8.git`  

### Install the system requirements (for Debian like)

` $ sudo apt install libpq python3`  

### Install PostgreSQL database adapter for the Python

`$ pip install psycopg2` 

### Install Python requirements

`$ .venv/bin/pip install -r requirements.txt`  

### Create the virtual environment

`$ python3 -m venv .venv`  

### Activate virtual environement  

`$ source .venv/bin/activate`

### Import database

`$ sudo psql -U postgres`

```psql
postgres=# CREATE DATABASE purbeurre;
postgres=# \q
```

`$ pg_restore -U postgres -d purbeurre [path]/fulldb.dump`

### Run server

`$ cd purbeurre/purbeurre_project && python manage.py runserver`  

## How to build statics

Static files are into purbeurre/purbeurre_project/static/  

### Install dependencies

`$ npm run install .` Install all dependencies.  

### Build statis

`$ npm run build` Create dist directory that contains all build static files served.  