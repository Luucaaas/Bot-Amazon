from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

def proceed_to_checkout(driver):
    try:
        print("🔍 Recherche du bouton 'Validez votre commande'...")
        iframe = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[8]/div/div/div/div/iframe")))
        driver.switch_to.frame(iframe)
        print("✅ Passé dans le contexte du pop-up.")
        
        
        # Chercher le bouton
        button_xpath =  "/html/body/div[4]/div[1]/div/div/div/div[2]/div/form/div/span/span/span/input"  
        button_element = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, button_xpath))
        )

        # Scroll pour le rendre visible
        driver.execute_script("arguments[0].scrollIntoView();", button_element)
    

        # Cliquer sur le bouton
        button_element.click()
        print("✅ Commande validée avec succès !")
    
    except TimeoutException:
        print("❌ Le bouton 'Validez votre commande' n'a pas été trouvé.")
    except Exception as e:
        print(f"⚠️ Erreur inattendue : {e}")
