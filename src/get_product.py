import os
import sys
from config import resource_path

def get_product_url():
    file_path = resource_path("product_url.txt")
    #file_path = resource_path("assets/product_url.txt")

    if not os.path.exists(file_path):
        raise FileNotFoundError(f"❌ Le fichier {file_path} est introuvable.")

    with open(file_path, "r", encoding="utf-8") as f:
        return f.read().strip()
