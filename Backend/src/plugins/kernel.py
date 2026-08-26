import importlib
import json
from pathlib import Path

from .registry import registry
from .base import PluginBase


class PluginKernel:
    def __init__(self):
        self.plugin_dir = Path(__file__).parent / "plugins_enabled"

    def load_plugins(self):
        for plugin_folder in self.plugin_dir.iterdir():
            manifest_file = plugin_folder / "manifest.json"
            plugin_file = plugin_folder / "plugin.py"

            if not manifest_file.exists() or not plugin_file.exists():
                continue

            manifest = json.loads(manifest_file.read_text())

            module_path = f"plugins.plugins_enabled.{plugin_folder.name}.plugin"
            module = importlib.import_module(module_path)

            plugin_class = getattr(module, manifest["class"])
            plugin_instance = plugin_class()

            registry.register(plugin_instance)
            plugin_instance.init()

            print(f"[PLUGIN] Chargé : {plugin_instance.name} v{plugin_instance.version}")

    def run_plugin(self, name, *args, **kwargs):
        plugin = registry.get(name)
        if not plugin:
            print(f"[PLUGIN] Introuvable : {name}")
            return None

        return plugin.run(*args, **kwargs)


kernel = PluginKernel()
