#encoding: utf-8

from settings import *

DEBUG = False

ALLOWED_HOSTS = [
    '*'
]


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', 
        'NAME': 'route',   
        'USER': 'postgres', 
        'PASSWORD': '', 
        'HOST': 'localhost',  
        'PORT': '5432', 
        }
}