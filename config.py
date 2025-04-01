import json

CONFIG_FILE = "config.json"

# Charger les identifiants
def load_config():
    with open(CONFIG_FILE, "r") as file:
        return json.load(file)

config = load_config()

EMAIL = config["email"]
PASSWORD = config["password"]
