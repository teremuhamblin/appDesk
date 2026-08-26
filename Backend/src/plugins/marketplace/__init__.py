"""
appDesk Plugin Marketplace
--------------------------

Ce module fournit :
- le système d'installation de plugins (ZIP / GitHub),
- la validation des manifests,
- la gestion des dépôts distants,
- l'intégration automatique avec le Plugin Kernel.

Modules exposés :
- installer : installation automatique
- repository : téléchargement / extraction
- validator : validation du manifest
"""

from .installer import install_from_zip
from .repository import download_zip, extract_zip
from .validator import validate_manifest

__all__ = [
    "install_from_zip",
    "download_zip",
    "extract_zip",
    "validate_manifest",
]
