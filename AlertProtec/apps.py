from django.apps import AppConfig


class AlertprotecConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'AlertProtec'
    
    def ready(self):
        import AlertProtec.signals
