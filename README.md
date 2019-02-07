# Book Sorter

A simple web application to sort books. 


## Features

- Django 2.1+
- Development, Staging and Production settings with [python-decouple](https://pypi.org/project/python-decouple/) 
- API with [Django Rest Framework](https://www.django-rest-framework.org/)


## Requirements

- Python >= 3.6


## How to install

> Remember to create a new virtualenv first
```bash

```


## Custom django settings

You must create a settings.ini file at the root of the project. To create this file, use the settings.ini.example template.

```
$ cp settings.ini.example settings.ini 
```

Default settings for settings.ini file.
These settings(and their default values) are used on development, staging and production environments.

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
    