from django.apps import AppConfig


class Config(AppConfig):
    name = 'ox_scale.apps.user_admin'  # ugh, why can't I just use 'user_admin' ?

    def ready(self):
        from  .. import signals
