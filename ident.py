import time
import config  # Import des identifiants depuis config.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

def login_amazon(driver, email, password):
    """Gère l'identification automatique sur Amazon si la page de connexion apparaît."""
    try:
        driver.get("https://www.amazon.fr/ap/signin?openid.pape.max_auth_age=900&openid.return_to=https%3A%2F%2Fwww.amazon.fr%2Fgp%2Fyourstore%2Fhome%3Fpath%3D%252Fgp%252Fyourstore%252Fhome%26signIn%3D1%26useRedirectOnSuccess%3D1%26action%3Dsign-out%26ref_%3Dnav_AccountFlyout_signout&openid.assoc_handle=frflex&openid.mode=checkid_setup&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0")
        print("🔑 Ouverture de la page de connexion Amazon...")

        # Attendre et renseigner l'email
        email_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "ap_email"))
        )
        email_input.send_keys(email)
        driver.find_element(By.ID, "continue").click()
        print("📩 Email renseigné.")

        # Attendre et renseigner le mot de passe
        password_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "ap_password"))
        )
        password_input.send_keys(password)
        driver.find_element(By.ID, "signInSubmit").click()
        print("🔓 Connexion en cours...")

        # Vérifier si la connexion a réussi
        time.sleep(3)
        if "ap/signin" in driver.current_url:
            print("❌ Erreur : Identifiants incorrects ou validation OTP requise.")
            return False

        print("✅ Connexion réussie.")
        return True

    except (TimeoutException, NoSuchElementException) as e:
        print(f"⚠️ Problème lors de l'identification : {e}")
        return False
