import json

PRODUCT_URL = "https://www.amazon.fr/JCC-Pok%C3%A9mon-boosters-%C3%89carlate-N%C3%A9buleuse-boosters/dp/B0DBK5B4XX?ref_=ast_sto_dp"
CONFIG_FILE = "config.json"

# Charger les identifiants
def load_config():
    with open(CONFIG_FILE, "r") as file:
        return json.load(file)

config = load_config()

EMAIL = config["email"]
PASSWORD = config["password"]
