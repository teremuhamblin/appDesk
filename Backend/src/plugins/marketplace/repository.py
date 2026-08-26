import requests
import zipfile
import io
from pathlib import Path

PLUGIN_DIR = Path(__file__).resolve().parent.parent / "plugins_enabled"

def download_zip(url):
    response = requests.get(url)
    return zipfile.ZipFile(io.BytesIO(response.content))

def extract_zip(zip_file, plugin_name):
    target = PLUGIN_DIR / plugin_name
    target.mkdir(exist_ok=True)
    zip_file.extractall(target)
    return target
