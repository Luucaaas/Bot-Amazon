from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def login_amazon(driver, email, password):
    """Gère l'identification si la page de connexion apparaît."""
    try:
        # Vérifier si le champ email est présent
        email_input = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.ID, "ap_email"))
        )
        email_input.send_keys(email)

        # Cliquer sur "Continuer"
        continue_button = driver.find_element(By.ID, "continue")
        continue_button.click()

        # Attendre l'apparition du champ mot de passe
        password_input = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.ID, "ap_password"))
        )
        password_input.send_keys(password)

        # Cliquer sur "Se connecter"
        sign_in_button = driver.find_element(By.ID, "signInSubmit")
        sign_in_button.click()

        print("✅ Connexion réussie.")

    except Exception as e:
        print(f"❌ Problème lors de l'identification : {e}")
