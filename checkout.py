from selenium.webdriver.common.by import By

def proceed_to_checkout(driver):
    """Passe à l’étape de paiement."""
    try:
        checkout_button = driver.find_element(By.ID, "hlb-ptc-btn-native")
        checkout_button.click()
        print("Passage au paiement initié.")
    except:
        print("Impossible d’accéder au paiement.")
