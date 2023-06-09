from .base import *

DEBUG = False

ALLOWED_HOSTS = [
    "54.178.179.97"
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'test',
        'USER': 'root',
        'PASSWORD': '1234',
        'HOST': '54.178.179.97',
        'PORT': '3306'
    }
}