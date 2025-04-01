from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def skip_prime_offer(driver):
    """Vérifie si la page de l'offre Prime s'affiche et clique sur 'Continuer sans les avantages Prime'."""
    try:
        # Attendre que le bouton apparaisse
        prime_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Continuer sans les avantages Prime')]"))
        )
        prime_button.click()
        print("✅ Offre Prime ignorée avec succès.")
    except Exception:
        print("ℹ️ Aucune offre Prime détectée, passage à l'étape suivante.")
