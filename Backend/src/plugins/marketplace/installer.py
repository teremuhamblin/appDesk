from .repository import download_zip, extract_zip
from .validator import validate_manifest
from plugins.kernel import kernel

def install_from_zip(url):
    zip_file = download_zip(url)
    plugin_name = url.split("/")[-1].replace(".zip", "")
    path = extract_zip(zip_file, plugin_name)

    manifest = validate_manifest(path)
    kernel.load_plugins()

    return {"installed": manifest["name"], "version": manifest["version"]}
