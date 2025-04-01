from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import time

def accept_cookies(driver):
    """Vérifie et accepte les cookies si la pop-up est présente."""
    try:
        cookies_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "sp-cc-accept"))
        )
        cookies_button.click()
        print("Cookies acceptés.")
        time.sleep(2)  # Petite pause pour éviter les bugs
    except NoSuchElementException:
        print("Pas de pop-up cookies détecté.")
    except TimeoutException:
        print("Timeout pendant l'attente des cookies.")

def check_seller_and_sender(driver):
    """Vérifie si le produit est vendu et expédié par Amazon."""
    try:
        # Trouver "Vendu par" (premier élément)
        seller_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '(//span[text()="Vendu par"])[1]'))
        )

        # Trouver "Amazon" (pour "Vendu par")
        amazon_seller_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '(//span[text()="Amazon"])[1]'))
        )

        # Vérifier si les deux éléments "Vendu par" et "Amazon" sont présents et corrects
        if seller_element.text == "Vendu par" and amazon_seller_element.text == "Amazon":
            print("✅ Le produit est bien vendu par Amazon.")
        else:
            print("❌ Le produit n'est pas vendu par Amazon.")
            return False  # Produit invalide

        # Maintenant vérifier si le produit est "Expédié par Amazon"
        shipper_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '(//span[text()="Expédié par"])[1]'))
        )

        # Trouver "Amazon" (pour "Expédié par")
        amazon_shipper_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '(//span[text()="Amazon"])[1]'))
        )

        # Vérifier si les deux éléments "Expédié par" et "Amazon" sont présents et corrects
        if shipper_element.text == "Expédié par" and amazon_shipper_element.text == "Amazon":
            print("✅ Le produit est bien expédié par Amazon.")
            return True  # Produit valide
        else:
            print("❌ Le produit n'est pas expédié par Amazon.")
            return False  # Produit invalide

    except Exception as e:
        print(f"Erreur dans la vérification du vendeur et expéditeur : {e}")
        return False  # En cas d'erreur, retourner False

def check_availability(driver):
    """Vérifie si le produit est en stock et vendu et expédié par Amazon."""
    accept_cookies(driver)  # Gérer les cookies avant de vérifier la disponibilité

    try:
        # Vérifier la disponibilité du produit
        stock_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "availability"))
        )
        stock_text = stock_element.text.strip()
        print("Disponibilité :", stock_text)

        # Vérifier si le produit est en stock
        if "en stock" in stock_text.lower():
            # Si le produit est en stock, vérifier le vendeur et l'expéditeur
            return check_seller_and_sender(driver)
        else:
            print("❌ Produit indisponible. Fermeture du bot.")
            driver.quit()
            exit()  # Ferme proprement le bot
    except NoSuchElementException:
        print("⚠️ Impossible de récupérer la disponibilité du produit. Fermeture du bot.")
        driver.quit()
        exit()  # Ferme proprement le bot
    except TimeoutException:
        print("Timeout pendant l'attente de l'élément 'Disponibilité'.")
        driver.quit()
        exit()  # Ferme proprement le bot
