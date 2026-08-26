"""
appDesk Plugin API
------------------

API REST permettant :
- de lister les plugins installés,
- d'exécuter un plugin,
- d'installer un plugin via URL.

Modules exposés :
- views : endpoints REST
- urls : routes de l'API
"""

from .views import PluginList, PluginRun, PluginInstall

__all__ = [
    "PluginList",
    "PluginRun",
    "PluginInstall",
]
