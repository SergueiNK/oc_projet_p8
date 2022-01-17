# oc_projet_p8

Créez une plateforme pour amateurs de Nutella

## About that Readme

Accéder au site

## https://purbeurre-spatial.herokuapp.com/

Develop into branch develop. Thank to change if you want to see the progress work

## How to build and run the HTTP server

### Clone the repo

`$ git clone: https://github.com/SergueiNK/oc_projet_p8.git`  

### Install the system requirements (for Debian like)

` $ sudo apt install libpq python3`  

### Install PostgreSQL database adapter for the Python

`$ pip install psycopg2` 

### Install Python requirements for linux

`$ .venv/bin/pip install -r requirements.txt`

### Install Python requirements for windows

`cd .venv/Scripts/`

`pip install -r ../../requirements.txt`

### Create the virtual environment

`$ python3 -m venv .venv`  

### Activate virtual environement  

`$ source .venv/bin/activate`

### Create database purbeurre

`$ sudo psql -U postgres`

```psql
postgres=# CREATE DATABASE your_database_name;
postgres=# \q
```
### Connect Django to Postgres project account

`$ cd config/settings`
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_database_name',
        'USER': 'your_username',
        'PASSWORD': 'your_password',
        'HOST': '',
        'PORT': '5432',
    }
}
```

### Import models to create tables

`$ python manage.py makemigrations` 

`$ python manage.py migrate` 

### Import and insert data from API Openfoodsfacts

`$ python manage.py download_data` 

### Run server

`$ cd purbeurre/purbeurre_project && python manage.py runserver`  

## How to build statics

Static files are into purbeurre/purbeurre_project/static/  

### Install dependencies

`$ npm run install .` Install all dependencies.  

### Build statis

`$ npm run build` Create dist directory that contains all build static files served.  