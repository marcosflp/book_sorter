# Book Sorter

A simple web application to sort books. 


## Features

- Django 2.1+
- API with [Django Rest Framework](https://www.django-rest-framework.org/)
- Custom some django settings with [python-decouple](https://pypi.org/project/python-decouple/) 


## Requirements

- Python >= 3.6


## How to configure and run the project

> Remember to create a new virtualenv first
```bash
$ git clone git@github.com:marcosflp/book_sorter.git
$ cd book_sorter
$ pip install -r requirements.txt
```


#### Custom django settings

You must create a settings.ini file at the root of the project. 
To create this file, use the settings.ini.example template.

```
$ cp settings.ini.example settings.ini 
```

> You don't need to change the the settings to run the project.

Default settings that you can change on the settings.ini file.
```
# Security
DEBUG=True
SECRET_KEY=4cn68iga94@**2x9vb1f*-104pe%%*-u-%%#%%1wh!r(+mjiza@y$

# Database
DATABASE_ENGINE=django.db.backends.postgresql_psycopg2
DATABASE_HOST=localhost
DATABASE_NAME=process_manager
DATABASE_USER=
DATABASE_PASSWORD=

# Logging
ENABLE_LOGGING=True

# Debug Toolbar
ENABLE_DEBUG_TOOLBAR=False
```
You can use these settings to configure different values to use in different
environments.

##### Running migration and create a superuser to access the system

```bash
$ python manage.py migrate
$ python manage.py createsuperuser
```

#### Running the project

```bash
$ python manage.py runserver
```


#### Running the tests

```bash
$ python manage.py test
```

## How to Use

The book sorting resource is available at: `/api/v1/sort_books/`


#### Example
Ordering a list of books by title ascending, author descending
and case insensitive
```
POST /api/v1/sort_books/?ordering=title,-author&case_insensitive=true
[
    {"title": "Java How to Program", "author": "Deitel & Deitel", "edition_year": 2007},
    {"title": "Patterns of Enterprise Application", "author": "Martin Fowler", "edition_year": 2002},
    {"title": "Head First Desing Patterns", "author": "Elisabeth Freeman", "edition_year": 2004},
    {"title": "Internet & World Wide Web: How to Program", "author": "Deitel & Deitel", "edition_year": 2007}
]
```
> To sort by descending order add a '-' at the beginning of the field you want. E.g: -title

> To define if the ordering is case insensitive add the param `case_insensitive=true` to the url. This param is optional.

Available fields to use on the ordering param.
- title
- author
- edition_year
