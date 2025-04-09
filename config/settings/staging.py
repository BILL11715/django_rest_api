from .base import *
from .base import config

import dj_database_url

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config("DB_NAME"),
        'USER': config("DB_USER"),
        'PASSWORD': config("DB_PASSWORD"),
        'HOST': config("DB_HOST", "localhost"),
        'PORT': config("DB_PORT"),
    }
}

DATABASES = {
    'default': dj_database_url.config(
        default=config('DATABASE_URL'),
        engine='django.contrib.gis.db.backends.postgis'
    )
}
