class PermissionDenied(Exception):
    pass


def check_permissions(plugin, required):
    for perm in required:
        if perm not in plugin.permissions:
            raise PermissionDenied(f"Permission '{perm}' manquante pour {plugin.name}")
