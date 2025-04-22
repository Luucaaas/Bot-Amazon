import os
import sys
import json

def resource_path(relative_path):
    """Retourne le chemin absolu vers un fichier depuis la racine du projet."""
    if getattr(sys, 'frozen', False):
        base_path = os.path.dirname(sys.executable)
    else:
        base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    return os.path.join(base_path, relative_path)


def load_config():
    #config_path = resource_path(os.path.join("assets", "config.json"))
    config_path = resource_path(os.path.join("config.json"))
    with open(config_path, "r", encoding="utf-8") as file:
        return json.load(file)

config = load_config()
EMAIL = config["email"]
PASSWORD = config["password"]
TRY = config["try"]
