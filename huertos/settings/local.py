from huertos.settings.base import *


DEBUG = True
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'huertos',                      
        'HOST': '',
        'PORT': 5432
    }
}