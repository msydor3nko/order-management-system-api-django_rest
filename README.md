# Order Management System API Guide

The simple API for Order Management System in electronics store
based on Django Rest Framework.


## Local DevEnv Setup

Clone the App repository using Git:

`git clone https://github.com/msydor3nko/order-management-system-api-django_rest.git`

Create and setup virtual environment:

`cd order-management-system-api-django_rest`  
`python3 -m venv venv`  
`source venv/bin/activate`

Update Pip and install dependencies:

`pip install -U pip`  
`pip install -r requirements.txt`


## Projet Setup

Make migrations:

`python manage.py migrate`


Load products data from fixtures (orders.json also there):

`python manage.py loaddata orders/fixtures/products.json`


## Setup Django Admin

Create superuser to use Django Admin (following console instructions):

`python manage.py createsuperuser`


## Run API

`python manage.py runserver`

You can use Django Admin for managing products and orders:

`http://127.0.0.1:8000/admin`


## Browsable API
You can use Browsable API provided by Django Rest Framework to requests endpoints.

Try to get order list, for example:
`http://127.0.0.1:8000/api/v1/orders/`


## Documentation

You can use Swagger or ReDoc to explore project endpoints:

#### Swagger 
`http://127.0.0.1:8000/swagger/`

#### ReDoc
`http://127.0.0.1:8000/redoc/`