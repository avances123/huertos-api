from django.apps import AppConfig
from actstream import registry

class FarmConfig(AppConfig):
    name = 'farms'

    def ready(self):
        registry.register(self.get_model('Farm'))