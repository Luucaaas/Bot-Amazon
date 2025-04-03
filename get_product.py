import os
import sys

def get_product_url():
    # Vérifie si le script est exécuté depuis un exécutable PyInstaller
    if getattr(sys, 'frozen', False):  
        base_path = os.path.dirname(sys.executable)  # Récupère le dossier de l'exécutable
    else:
        base_path = os.path.dirname(os.path.abspath(__file__))  # Mode script Python normal

    file_path = os.path.join(base_path, "product_url.txt")  # Chemin absolu

    # Vérifie si le fichier existe
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Le fichier {file_path} est introuvable.")

    with open(file_path, "r") as f:
        return f.read().strip()
