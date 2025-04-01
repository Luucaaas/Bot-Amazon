import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException

def accept_cookies(driver):
    """Vérifie et accepte les cookies si la pop-up est présente."""
    try:
        cookies_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "sp-cc-accept"))
        )
        cookies_button.click()
        print("Cookies acceptés.")
        time.sleep(2)  # Petite pause pour éviter les bugs
    except (NoSuchElementException, TimeoutException):
        print("Pas de pop-up cookies détectée ou timeout.")

def check_seller_and_sender(driver):
    """Vérifie si le produit est vendu et expédié par Amazon."""
    try:
        # Vérifier "Vendu par Amazon"
        seller_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '(//span[text()="Vendu par"])[1]'))
        )
        amazon_seller_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '(//span[text()="Amazon"])[1]'))
        )

        # Vérifier "Expédié par Amazon"
        shipper_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '(//span[text()="Expédié par"])[1]'))
        )
        amazon_shipper_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '(//span[text()="Amazon"])[1]'))
        )

        # Vérifier les conditions
        if (
            seller_element.text == "Vendu par" and amazon_seller_element.text == "Amazon"
            and shipper_element.text == "Expédié par" and amazon_shipper_element.text == "Amazon"
        ):
            print("✅ Le produit est vendu et expédié par Amazon.")
            return True
        else:
            print("❌ Le produit n'est pas vendu ou expédié par Amazon.")
            return False

    except Exception as e:
        print(f"⚠️ Erreur dans la vérification du vendeur/expéditeur : {e}")
        return False

def check_availability(driver, max_retries=1, refresh_interval=45):
    """Vérifie si le produit est en stock et vendu/expédié par Amazon.
       Rafraîchit la page toutes les 45 secondes jusqu'à `max_retries` tentatives.
    """
    accept_cookies(driver)  # Gérer les cookies avant de vérifier la disponibilité

    for attempt in range(1, max_retries + 1):
        try:
            print(f"🔄 Vérification du stock (tentative {attempt}/{max_retries})...")
            
            # Vérifier la disponibilité du produit
            stock_element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "availability"))
            )
            stock_text = stock_element.text.strip()
            print("📦 Disponibilité :", stock_text)

            # Vérifier si le produit est en stock
            if "en stock" in stock_text.lower():
                # Vérifier le vendeur et l'expéditeur
                if check_seller_and_sender(driver):
                    print("✅ Le produit est disponible et vendu/expédié par Amazon.")
                    return True  # On continue le programme
                else:
                    print("❌ Le produit n'est pas vendu/expédié par Amazon.")
            else:
                print("❌ Produit toujours indisponible.")

        except (NoSuchElementException, TimeoutException):
            print("⚠️ Impossible de récupérer la disponibilité du produit.")
        
        # Si on arrive ici, c'est que le produit n'est pas dispo => on attend et on rafraîchit
        if attempt < max_retries:
            print(f"🕒 Attente de {refresh_interval} secondes avant de rafraîchir...")
            time.sleep(refresh_interval)
            driver.refresh()
        else:
            print("❌ Le produit est toujours indisponible après plusieurs tentatives.")
            driver.quit()
            exit()  # Fermeture propre du bot

    return False  # Cas de sortie si jamais atteint
