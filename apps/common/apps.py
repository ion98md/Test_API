from django.apps import AppConfig


class CommonConfig(AppConfig):
    name = "apps.common"
    label = "common"

    def ready(self):
        ...
