import time
import sys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from kpi import send_kpi_to_bigquery
import get_product as get_product
from config import EMAIL
from config import TRY


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
    print("🔍 Vérification du vendeur et de l'expéditeur...")

    def find_amazon_label(keywords):
        candidates = driver.find_elements(By.XPATH, "//span | //div")
        for element in candidates:
            try:
                text = element.text.strip().lower()
                if any(kw in text for kw in keywords) and "amazon" in text:
                    print(f"✅ Détection d'un bloc contenant '{keywords}' et 'Amazon' : {text}")
                    return True
            except Exception:
                continue
        return False

    sold_by_amazon = find_amazon_label(["vendu par", "vendu et expédié par"])
    shipped_by_amazon = find_amazon_label(["expédié par", "vendu et expédié par"])

    if sold_by_amazon and shipped_by_amazon:
        print("✅ Le produit est vendu **et** expédié par Amazon.")
        return True
    else:
        if not sold_by_amazon:
            print("❌ Vendeur Amazon non détecté.")
        if not shipped_by_amazon:
            print("❌ Expéditeur Amazon non détecté.")
        return False


def check_availability(driver, max_retries=TRY, refresh_interval=45):
    accept_cookies(driver)
    account_id = EMAIL
    PRODUCT_URL = get_product.get_product_url()

    def find_real_stock_element(driver):
        possible_spans = driver.find_elements(By.XPATH, "//span[contains(translate(text(), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'en stock')]")
        for span in possible_spans:
            try:
                if span.is_displayed():
                    parent = span.find_element(By.XPATH, "./ancestor::div[1]")
                    parent_html = parent.get_attribute("outerHTML")
                    if "availability" in parent_html or "buybox" in parent_html or "a-color-success" in span.get_attribute("class"):
                        return span
            except Exception:
                continue
        return None

    for attempt in range(1, max_retries + 1):
        try:
            print(f"🔄 Vérification du stock (tentative {attempt}/{max_retries})...")

            stock_element = find_real_stock_element(driver)

            if stock_element:
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
                    send_kpi_to_bigquery("not_available", account_id, PRODUCT_URL)
            else:
                print("⚠️ Aucun élément 'En stock' pertinent trouvé.")
                send_kpi_to_bigquery("out_of_stock", account_id, PRODUCT_URL)

        except (NoSuchElementException, TimeoutException):
            print("⚠️ Erreur lors de la recherche de l’élément 'En stock'.")
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
