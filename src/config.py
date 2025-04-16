import os
import sys
import json

def resource_path(relative_path):
    """Retourne le bon chemin vers un fichier, que ce soit en local ou via PyInstaller."""
    try:
        base_path = sys._MEIPASS  # utilisé quand exécuté avec PyInstaller
    except AttributeError:
        base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    return os.path.join(base_path, relative_path)

def load_config():
    config_path = resource_path(os.path.join("assets", "config.json"))
    #config_path = resource_path(os.path.join("config.json"))
    with open(config_path, "r", encoding="utf-8") as file:
        return json.load(file)

config = load_config()
EMAIL = config["email"]
PASSWORD = config["password"]
