from django.apps import AppConfig
from django.core.signals import request_finished


class PublicationsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.publications'

    def ready(self):
        from .import signals
       # request_finished.connect(publication_handler)