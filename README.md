# fresh-food
Minor Project  #3 Fresh Food by Team 13


# Links
* Postman API Team Invite Link: https://app.getpostman.com/join-team?invite_code=58b9cf96a113199173c6956c32ab1145
* Postman API Team Link: https://ece567-fall21-team13.postman.co/workspace


# How to run
1. Activate the environment with -
> source venv/bin/activate
2. Set the appropriate env vars as necessary - 
```shell
export FLASK_ENV=development
export FLASK_DEBUG=1
export FLASK_APP=autoapp.py
```
3. Run the development server with current directory fresh-food/backend
> ../venv/bin/python -m flask run

# How to setup database - 
1. Setup postgres in your machine with your OS specific instructions -
```shell
# For debian - 
sudo apt install postgresql-13 postgresql-client postgresql-doc libpq-dev
```
2. Create database in your system -
```shell
psql -U postgres 

# Now in psql shell
create database fresh_food
```
3. Run all the sql in file -> [db.sql](backend/db.sql) with altering  paths as per your system

# Where's the documentation? 
The documentation is [docs](docs) folder of this repo. 
Also, all dirs like backend, frontend have their own README.md for explanation. 

# REPO URL - 
The original repo was - https://github.com/ece567-fall21-team13/fresh-food
We used this because there was no repo shared from radical then. 
We'll migrate all commits to radical repo once we close our **iteration3**
