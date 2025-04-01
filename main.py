import config
from config import EMAIL,PASSWORD
from amazon_bot import AmazonBot
from availability import check_availability
from cart import buy_now
from ident import login_amazon
from prime import skip_prime_offer
from checkout import proceed_to_checkout

# Initialisation du bot
bot = AmazonBot()
bot.open_product_page(config.PRODUCT_URL)

# Vérification du stock et du vendeur
check_availability(bot.driver)  # Le bot quitte déjà si le produit ne convient pas

# Si le produit est en stock et vendu par Amazon, on continue
buy_now(bot.driver)
login_amazon(bot.driver,EMAIL,PASSWORD)
skip_prime_offer(bot.driver)



#proceed_to_checkout(bot.driver)
input("Appuyez sur Entrée pour fermer le navigateur...")

bot.close_browser()
