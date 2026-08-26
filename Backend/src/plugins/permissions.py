class PermissionDenied(Exception):
    pass

PERMISSIONS = {
    "read": "Lecture basique",
    "write": "Écriture basique",
    "network": "Accès réseau",
    "filesystem": "Accès au système de fichiers",
    "database": "Accès à la base de données",
}

def check_permissions(plugin, required):
    for perm in required:
        if perm not in plugin.permissions:
            raise PermissionDenied(
                f"Permission '{perm}' manquante pour {plugin.name}"
            )
