from django.apps import AppConfig
from .kernel import kernel

class PluginLoader(AppConfig):
    name = "plugins"

    def ready(self):
        kernel.load_plugins()
