import config
import get_product
from config import EMAIL,PASSWORD
from amazon_bot import AmazonBot
from availability import check_availability
from cart import buy_now
from ident import login_amazon
from prime import skip_prime_offer
from checkout import proceed_to_checkout

# Initialisation du bot
bot = AmazonBot()
login_amazon(bot.driver,EMAIL,PASSWORD)

PRODUCT_URL = get_product.get_product_url()
bot.open_product_page(PRODUCT_URL)
# Vérification du stock et du vendeur
check_availability(bot.driver)  # Le bot quitte déjà si le produit ne convient pas

# Si le produit est en stock et vendu par Amazon, on continue
buy_now(bot.driver)

skip_prime_offer(bot.driver)

proceed_to_checkout(bot.driver)

bot.close_browser()
