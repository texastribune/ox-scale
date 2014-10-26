from django.apps import AppConfig


class Config(AppConfig):
    name = 'ox_scale.apps.scale'  # ugh, why can't I just use 'scale'?

    def ready(self):
        from  .. import signals
