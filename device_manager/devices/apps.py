from django.apps import AppConfig

started = False

class DevicesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'devices'
    def ready(self):
        
        from . import signals  # Import and register signals

        from .mqtt_consumer import client
        client.loop_start()


    