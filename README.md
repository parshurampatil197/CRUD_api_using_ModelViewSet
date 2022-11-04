

## CRUD_api_using_ModelViewSet



# Description

I have created REST API in Django Using DRF. created the class-based view. We will use the ModelViewSet class, a subclass of Django's View class. 
We can define the get(), post(), put(), and delete() methods so that we can perform the CRUD operations.


## Requirements

Last tested successfully with Python 3.6.19 and Ubuntu 16.04\
Django==2.2\
djangorestframework==3.10.2


[Django](https://www.djangoproject.com/): The web framework for perfectionists with deadlines (Django builds better web apps with less code).

[DRF](https://github.com/gitgik/django-rest-api/blob/master/www.django-rest-framework.org): A powerful and flexible toolkit for building Web APIs


## Quick Setup

1. Create a folder for your project on your local machine
```bash
  mkdir myproject; 
  cd myproject

```

2. Download this project template from GitHub

```bash
  git clone https://github.com/parshurampatil197/CRUD_api_using_ModelViewSet.git
  cd CRUD_api_using_ModelViewSet
  
```

3. Create a virtual environment and install django
```bash
  virtualenv venv --python=python3 ; 
  source venv/bin/activate; 

```

4. Install the dependencies needed to run the app:
```bash
  pip install -r requirements

```

5. Initialize the database

```bash
  python manage.py makemigrations
  python manage.py migrate

```


6. Run the project

```bash
  python manage.py runserver

```






## API Reference
 
Test API by Using chrome
#### Http request: POST 

```http
  http://127.0.0.1:8000/v1/book
```


#### Http request: GET 

```http
  http://127.0.0.1:8000/v1/book
```

```http
  http://127.0.0.1:8000/v1/book/1
```



#### Response

```http
[
    {
        "id": 1,
        "name": "A SONG OF ICE AND FIRE",
        "author": "George R. R. Martin"
    },
    {
        "id": 2,
        "name": "A Dance with Dragons",
        "author": "George R. R. Martin"
    },
    {
        "id": 3,
        "name": "A Feast for Crows",
        "author": "George R. R. Martin"
    }
]
```


#### Http request: PUT 

```http
 http://127.0.0.1:8000/v1/book/1
```

#### Http request: DELETE 

```http
  http://127.0.0.1:8000/v1/book/1
```


## Authors

- [@parshuram](https://github.com/parshurampatil197)

