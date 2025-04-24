from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementClickInterceptedException
from screenshot import take_screenshot_on_error
import time

def proceed_to_checkout(driver, timeout=10):
    print("🔍 Tentative d'accès au bouton 'Validez votre commande'...")

    try:
        
        iframe_xpath = '//*[@id="turbo-checkout-iframe"]'
        iframe = WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located((By.XPATH, iframe_xpath))
        )
        driver.switch_to.frame(iframe)
        print("✅ Passé dans le contexte du pop-up.")

        
        button_xpaths = [
            '//*[@id="turbo-checkout-pyo-button"]',
            '/html/body/div[4]/div[1]/div/div/div/div[2]/div/form/div/span/span/span/input'
        ]

        button_found = False

        for xpath in button_xpaths:
            try:
                print(f"🔎 Recherche du bouton via : {xpath}")
                button = WebDriverWait(driver, timeout).until(
                    EC.element_to_be_clickable((By.XPATH, xpath))
                )

                if button.is_displayed() and button.is_enabled():
                    driver.execute_script("arguments[0].scrollIntoView();", button)
                    button.click()
                    print("✅ Commande validée avec succès !")
                    button_found = True
                    break
                else:
                    print("⚠️ Bouton trouvé mais inactif.")
            except (TimeoutException, ElementClickInterceptedException):
                print(f"❌ Impossible de cliquer sur le bouton via : {xpath}")

        if not button_found:
            raise NoSuchElementException("Aucun des XPaths n'a permis de trouver un bouton cliquable.")

    except Exception as e:
        print(f"⚠️ Erreur critique lors de la validation de la commande : {e}")
        take_screenshot_on_error(driver)
