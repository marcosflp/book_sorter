# Book Sorter

A simple web application to sort books. 


## Features

- Django 2.1+
- API with [Django Rest Framework](https://www.django-rest-framework.org/)
- Custom some django settings with [python-decouple](https://pypi.org/project/python-decouple/) 


## Requirements

- Python >= 3.6


## How to configure and run the project

Download the project
```
$ git clone https://github.com/marcosflp/book_sorter.git
$ cd book_sorter
```


### 1. With Docker

1. Install [Docker](https://docs.docker.com/install/)
2. Install [Docker-compose](https://docs.docker.com/compose/install/)

##### Building and running the project
```
$ docker-compose up --build
or in a daemon mode
$ docker-compose --build -d
```

##### Running the tests
```
$ docker-compose run django python manage.py test
```


### 2. With a virtualenv

> Remember to create a new virtualenv first
```bash
$ pip install -r requirements.txt
$ python manage.py migrate
$ python manage.py runserver
```


##### Running the tests

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
