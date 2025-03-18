from django.apps import AppConfig


class MasterCollectionConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'master_collection'

    def ready(self):
        import master_collection.signals