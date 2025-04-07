import time
import sys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException

def accept_cookies(driver):
    """Vérifie et accepte les cookies si la pop-up est présente."""
    try:
        cookies_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.ID, "sp-cc-accept"))
        )
        cookies_button.click()
        print("✅ Cookies acceptés.")
        time.sleep(2)
    except (NoSuchElementException, TimeoutException):
        print("ℹ️ Pas de pop-up cookies détectée.")

def check_seller_and_sender(driver):
    """Vérifie si le produit est vendu et expédié par Amazon."""
    try:
        seller_xpath = '//span[contains(text(),"Vendu par")]/following-sibling::span[contains(text(),"Amazon")]'
        shipper_xpath = '//span[contains(text(),"Expédié par")]/following-sibling::span[contains(text(),"Amazon")]'

        seller_element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, seller_xpath))
        )
        shipper_element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, shipper_xpath))
        )

        if seller_element and shipper_element:
            print("✅ Produit vendu et expédié par Amazon.")
            return True
    except TimeoutException:
        print("❌ Le produit n'est pas vendu/expédié par Amazon.")
    return False

def check_availability(driver, max_retries=10, refresh_interval=45):
    """Vérifie si le produit est en stock sur Amazon.
       Rafraîchit la page toutes les 45 secondes jusqu'à `max_retries` tentatives.
    """
    accept_cookies(driver)

    for attempt in range(1, max_retries + 1):
        try:
            print(f"🔄 Vérification du stock (tentative {attempt}/{max_retries})...")

            stock_xpath = "(//span[contains(@class, 'a-size-medium') and contains(@class, 'a-color-success') and contains(text(), 'En stock')])[2]"

            stock_element = WebDriverWait(driver, 5).until(
                EC.visibility_of_element_located((By.XPATH, stock_xpath))
            )

            driver.execute_script("arguments[0].scrollIntoView();", stock_element)
            time.sleep(1)

            stock_elements = driver.find_elements(By.XPATH, stock_xpath)
            if stock_elements:
                print(f"✅ Élément(s) trouvé(s) : {len(stock_elements)}")
                for elem in stock_elements:
                    try:
                        print(f"📌 Texte détecté : '{elem.text.strip()}'")
                    except:
                        print("⚠️ Erreur lors de la récupération du texte.")
            else:
                print("❌ Aucun élément 'En stock' trouvé.")

            stock_text = stock_element.text.strip()
            print(f"📦 Disponibilité détectée : {stock_text}")

            if "en stock" in stock_text.lower():
                print("✅ Le produit est disponible !")
                return True
            else:
                print("❌ Produit toujours indisponible.")

        except (NoSuchElementException, TimeoutException):
            print("⚠️ Produit non disponible ou l'élément 'En stock' est introuvable.")

        # ➕ Ajout ici : pour continuer sans crash
        if attempt < max_retries:
            print(f"🕒 Attente de {refresh_interval} secondes avant de rafraîchir...")
            time.sleep(refresh_interval)
            driver.refresh()
        else:
            print("❌ Le produit est toujours indisponible après plusieurs tentatives.")
            driver.quit()
            sys.exit()

    return False

