# Order Management System API Guide

## Projet Setup

---

## Load products data from fixtures 
 `python manage.py loaddata products.json`

## Create model fixtures from DB data
`python manage.py dumpdata orders.Product > fixtures.json`

---

## Documentation

### Swagger, ReDoc
You can use Swagger or ReDoc to explore project endpoints:

`http://127.0.0.1:8000/swagger/`  
`http://127.0.0.1:8000/redoc/`

### Browsable API
You can use Browsable API provided by Django Rest Framework to requests endpoints. Try to get order list, for example:

`http://127.0.0.1:8000/api/v1/orders/`
