from huertos.settings.base import *


DEBUG = True
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'huertos',                      
        'HOST': '',
        'PORT': 5433
    }
}