import time
import sys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from src.kpi import send_kpi_to_bigquery
import src.get_product as get_product
from src.config import EMAIL


def accept_cookies(driver):
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
    try:
        possible_selectors = [
            (By.ID, "merchant-info"),
            (By.XPATH, "//*[contains(text(), 'Expédié')]"),
            (By.XPATH, "//*[contains(text(), 'Vendu')]"),
        ]

        seller_texts = []

        for by, selector in possible_selectors:
            try:
                elements = driver.find_elements(by, selector)
                for el in elements:
                    text = el.text.strip()
                    if text:
                        seller_texts.append(text.lower())
            except:
                continue

        for text in seller_texts:
            if "expédié par amazon" in text and "vendu par amazon" in text:
                print("✅ Produit vendu et expédié par Amazon.")
                return True

        print("❌ Produit disponible mais pas vendu/expédié par Amazon.")
        return False

    except Exception as e:
        print(f"⚠️ Erreur lors de la vérification du vendeur : {e}")
        return False


def check_availability(driver, max_retries=10, refresh_interval=45):
    accept_cookies(driver)
    account_id = EMAIL
    PRODUCT_URL = get_product.get_product_url()

    for attempt in range(1, max_retries + 1):
        try:
            print(f"🔄 Vérification du stock (tentative {attempt}/{max_retries})...")

            stock_xpath = "//*[@id='availability']/span"

            stock_element = WebDriverWait(driver, 5).until(
                EC.visibility_of_element_located((By.XPATH, stock_xpath))
            )

            driver.execute_script("arguments[0].scrollIntoView();", stock_element)
            time.sleep(1)

            stock_text = stock_element.text.strip()
            print(f"📦 Disponibilité détectée : {stock_text}")

            if "en stock" in stock_text.lower():
                if check_seller_and_sender(driver):
                    print("✅ Le produit est disponible et conforme.")
                    send_kpi_to_bigquery("success", account_id, PRODUCT_URL)
                    return True
                else:
                    print("⚠️ Produit en stock mais pas vendu/expédié par Amazon.")
                    send_kpi_to_bigquery("wrong_seller", account_id, PRODUCT_URL)
                    return False
            else:
                print("❌ Produit toujours indisponible.")

        except (NoSuchElementException, TimeoutException):
            print("⚠️ Produit non disponible ou l'élément 'En stock' est introuvable.")
            send_kpi_to_bigquery("out_of_stock", account_id, PRODUCT_URL)

        if attempt < max_retries:
            print(f"🕒 Attente de {refresh_interval} secondes avant de rafraîchir...")
            time.sleep(refresh_interval)
            driver.refresh()
        else:
            print("❌ Le produit est toujours indisponible après plusieurs tentatives.")
            driver.quit()
            sys.exit()

    return False
