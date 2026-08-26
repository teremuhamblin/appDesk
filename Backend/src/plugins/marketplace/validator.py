import json

def validate_manifest(path):
    manifest = json.loads((path / "manifest.json").read_text())
    required = ["name", "version", "class", "description"]

    for key in required:
        if key not in manifest:
            raise Exception(f"Manifest invalide : {key} manquant")

    return manifest
