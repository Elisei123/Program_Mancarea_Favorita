## Installation
- install python libraries: `python3 -m pip install -r requirements.txt `
- run migrations: `python3 manage.py migrate`
- start the server: `python3 manage.py runserver`

##  Postgresql setup
#### terminal (bash)

- sudo apt update
- sudo apt install postgresql postgresql-contrib
- sudo -u postgres psql -c "SELECT version();   `->check version`
- sudo -u postgres psql 

- create database Eat_Smart;
- create user postgres2 with password 'Tmarcel21'; `PS: it is not universal :)`
