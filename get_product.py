def get_product_url(filename="product_url.txt"):
    """Lit l'URL du produit depuis un fichier texte."""
    try:
        with open(filename, "r", encoding="utf-8") as file:
            return file.readline().strip()  # Récupère la première ligne proprement
    except FileNotFoundError:
        print("❌ Erreur : Fichier 'product_url.txt' introuvable.")
        exit()
