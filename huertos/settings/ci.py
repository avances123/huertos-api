from huertos.settings.base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'huertos',                      
        'HOST': '',
        'PORT': 5432
    }
}