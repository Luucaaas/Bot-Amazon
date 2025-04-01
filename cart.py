from selenium.webdriver.common.by import By
import time

def add_to_cart(driver):
    """Ajoute le produit au panier."""
    try:
        add_to_cart_button = driver.find_element(By.ID, "add-to-cart-button")
        add_to_cart_button.click()
        print("Produit ajouté au panier.")
        time.sleep(2)  # Laisse le temps à la page de charger
    except:
        print("Échec de l'ajout au panier.")
