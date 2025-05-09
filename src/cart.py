from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from screenshot import take_screenshot_on_error

def buy_now(driver):
    """Clique sur le bouton Achat immédiat si disponible."""
    try:
        buy_now_button = WebDriverWait(driver, 1).until(
            EC.element_to_be_clickable((By.ID, "buy-now-button"))
        )
        buy_now_button.click()
        print("✅ Bouton 'Achat immédiat' cliqué avec succès.")


    except Exception as e:
        print(f"❌ Impossible de cliquer sur 'Achat immédiat' : {e}")
        take_screenshot_on_error(driver)
