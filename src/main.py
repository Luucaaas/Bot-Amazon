import os
import config as config
import get_product as get_product
from config import EMAIL, PASSWORD
from amazon_bot import AmazonBot
from availability import check_availability
from cart import buy_now
from ident import login_amazon
from prime import skip_prime_offer
from checkout import proceed_to_checkout
from kpi import send_kpi_to_bigquery
from config import EMAIL

# Configuration de l'authentification Google Cloud
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/Users/lucas/Desktop/Bot Amazon/assets/key.json"

# Initialisation du bot
bot = AmazonBot()

try:
    login_amazon(bot.driver, EMAIL, PASSWORD)

    PRODUCT_URL = get_product.get_product_url()
    bot.open_product_page(PRODUCT_URL)

    # Vérification du stock
    dispo = check_availability(bot.driver)

    if dispo:
        buy_now(bot.driver)
        skip_prime_offer(bot.driver)
        proceed_to_checkout(bot.driver)

except Exception as e:
    print(f"💥 Erreur critique : {e}")
    send_kpi_to_bigquery("error", EMAIL, PRODUCT_URL)

finally:
    bot.close_browser()
