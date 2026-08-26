class PluginBase:
    name = "UnnamedPlugin"
    version = "0.1"
    description = "No description"
    permissions = []

    def __init__(self):
        pass

    def init(self):
        """Chargé au démarrage du backend."""
        return True

    def run(self, *args, **kwargs):
        """Action principale du plugin."""
        raise NotImplementedError("run() doit être implémenté")

    def stop(self):
        """Arrêt propre du plugin."""
        return True
