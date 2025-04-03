import os
import sys 
import json

def load_config():
    # Obtenir le chemin absolu du fichier config.json
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    config_path = os.path.join(base_path, "config.json")

    # Charger la configuration
    with open(config_path, "r", encoding="utf-8") as file:
        return json.load(file)

config = load_config()

EMAIL = config["email"]
PASSWORD = config["password"]
