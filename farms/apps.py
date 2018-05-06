from django.apps import AppConfig

class FarmConfig(AppConfig):
    name = 'farms'

    def ready(self):
        from actstream import registry
        registry.register(self.get_model('Farm'))