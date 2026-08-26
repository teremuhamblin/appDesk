from plugins.base import PluginBase
from plugins.permissions import check_permissions

class ExamplePlugin(PluginBase):
    name = "ExamplePlugin"
    version = "1.0"
    description = "Plugin de démonstration"
    permissions = ["read"]

    def init(self):
        print("[ExamplePlugin] Initialisation OK")
        return True

    def run(self, data=None):
        check_permissions(self, ["read"])
        return {"message": "Plugin exécuté", "data": data}

    def stop(self):
        print("[ExamplePlugin] Arrêt propre")
        return True
