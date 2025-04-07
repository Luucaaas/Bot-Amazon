import os
import sys

def get_product_url():
    
    if getattr(sys, 'frozen', False):  
        base_path = os.path.dirname(sys.executable)  
    else:
        base_path = os.path.dirname(os.path.abspath(__file__))  

    file_path = os.path.join(base_path, "product_url.txt")  

    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Le fichier {file_path} est introuvable.")

    with open(file_path, "r") as f:
        return f.read().strip()
