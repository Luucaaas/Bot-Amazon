import os
import sys

def get_product_url():

    base_path = getattr(sys, '_MEIPASS', os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
    
    file_path = os.path.join(base_path, "assets", "product_url.txt")
    #file_path = os.path.join(base_path,"product_url.txt")


    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Le fichier {file_path} est introuvable.")

    with open(file_path, "r", encoding="utf-8") as f:
        return f.read().strip()