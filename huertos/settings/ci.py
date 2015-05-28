from huertos.settings.base import *

DATABASES = {
    'default': {
        #'ENGINE': 'django.db.backends.sqlite3',
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'huertos',                      
        'HOST': '',
        'PORT': 5432
    }
}