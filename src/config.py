import os
import sys
import json

def load_config():
    # Détecter si l'exécutable est lancé via PyInstaller
    base_path = getattr(sys, '_MEIPASS', os.path.abspath(os.path.dirname(__file__)))

    # Le fichier est à la racine (et non dans un dossier "assets")
    config_path = os.path.join(base_path, "config.json")

    # Charger la configuration
    with open(config_path, "r", encoding="utf-8") as file:
        return json.load(file)

config = load_config()

EMAIL = config["email"]
PASSWORD = config["password"]
