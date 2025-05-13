from django.apps import AppConfig

class AdminConfig(AppConfig):
    name = 'administrator'

    def ready(self):
        import administrator.signals
