# Campus Crud

Let's add basic crud operations to our first Django application.

## Setup

1) Clone this repository into your django-env directory (your virtual environment)

2) Update django version to 4.1 -  `pipenv install django==4.1` 

3) Windows users go to settings.py and add 'USER' and 'PASSWORD' to DATABASES config 

4) Start Server `python3 manage.py runserver`

4) Go to localhost:8000 to see index route "Welcome to our campus!"

**If you already have a 'campus' db with books:**

5) Go to localhost:8000/books/ to see all books in the DB

<br><br>


## Database Setup ( only if starting from scratch )

### Create DB

**Open the psql shell:**

`psql` OR `psql -U postgres` (on Windows)

Create a DB:

`CREATE DATABASE campus;`

Exit shell:

`\q`

<br><br>

### Make Migrations and Migrate

**Make migration** file(s):

`python3 manage.py makemigrations`

**Migrate** those files over to the DB to generate your tables:

`python3 manage.py migrate`

<br><br>

### Create Seed Data

Open Django ORM shell to easily add books to campus using book model:

Run : `python3 manage.py shell`

```shell
>>> from library.models import Book
>>> book = Book(title='The Cat in the Hat', author='Dr. Seuss')
>>> book.save()
```

Do this multiple times to create a few entries. 