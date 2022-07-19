# DDoS Simulator
This project simulates a DDoS on a mock server using Docker, Django, PostgreSQL, Redis, and Nginx.

## Setup
The project uses the following:
- Python 3.9
- Django 4.0.3
- PostgreSQL 14
- Redis 7
- Nginx 1.21
- Docker
- Docker Compose

For additional information on project specifications, see the 
```Pipfile``` in the ```api``` directory.

### Environment
In the ```api/``` directory, create a ```.env``` file
that contains the following environment variables:
```
SECRET_KEY=somerandomstring

DEBUG=False
ALLOWED_HOSTS=localhost 127.0.0.1
CORS_ALLOWED_ORIGIN_REGEXES=^https?://(localhost|127\.0\.0\.1)$

DB_ENGINE=django.db.backends.postgresql_psycopg2
DB_NAME=ddos_simulator
DB_HOST=postgres
DB_USER=postgres
DB_PASSWORD=password
DB_PORT=5432

REDIS_URL=redis://redis:6379/1
```
The database variables can be changed as desired. However, make sure to update
the environment variables in ```docker-compose.yml``` as well.

## Building
The project uses Docker. Ensure Docker and Docker Compose are installed before continuing.

To build, run ```docker-compose build```

## Running
To run the web API, run ```docker-compose up -d```, then go to 
http://localhost/api/core/data using your web browser. You should 
see a list of data. Initially, it will be empty.

## Simulating a DDoS Attack
A directory called ```ddos``` provides a Python script and several
JSON files that are used to perform a DDoS attack. The modules needed
for the script can be found in ```requirements.txt```.

It is advised to set up a virtual environment.
To do so, ensure that you are in the ```ddos``` directory. Then
enter ```python -m venv venv```, then activate the virtual
environment using ```"./venv/Scripts/activate"``` if you are using 
Windows, or ```venv/bin/activate``` if you are using MacOS or Linux.

Then, in your virtual environment, run ```pip install -r requirements.txt```
to install the depedencies needed for the DDoS script. After that, you can
run a DDoS attack using ```python ddos_attack.py```.
