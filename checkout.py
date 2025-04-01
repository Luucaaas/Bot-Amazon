from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def proceed_to_checkout(driver):
    """Passe à l’étape de paiement et valide la commande."""
    try:
        # Attendre et cliquer sur "Passer au paiement"
        checkout_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//input[@id="hlb-ptc-btn-native"]'))
        )
        checkout_button.click()
        print("🛒 Passage au paiement initié.")

        # Attendre et cliquer sur "Validez votre commande"
        place_order_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//input[@id="turbo-checkout-place-order-button"]'))
        )
        place_order_button.click()
        print("✅ Commande validée avec succès !")

    except Exception as e:
        print(f"❌ Erreur lors du paiement : {e}")
