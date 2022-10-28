# portfolio

## Create env

Create a virtualenv in the directory of cloning repo to manage Python packages for different projects.

The command ```virtualenv -p python env``` create the virtual evironment for the project.

Now to activate the virtualenv go to the path where the env is created using terminal and write ```source env\bin\activate ``` .

## Clone the Repo

Now clone the repo and go to the path for requirements.txt, which contains all the packages required for running the project.

To install the packages from  requirements.txt write ```pip install -r requirements.txt``` in terminal.

## DataBase used

Postgres database with postgis is used in the project.

Create database and <b>run migrate command</b>.

When DEBUG is True, local settings will be used for local server and when the DEBUG in False, default settings is used defined in .env file and runs on prod or dev server.

## Create Migrations

To create migrations run ```python manage.py migrate``` command. This will create the tables in the database.

## Create SuperUser

To create superuser run command ```python manage.py createsuperuser```. This will create the superuser who has all the permission of admin site.

## Run Server

To run the server run command ```python manage.py runserver```. The project will run on localhost 8000. It will redirect first to the register page. If already existing user then click on ```click here``` button at the bottom to  login and if not then first register.

## .env File

This file contains all the static variables used  in the project.