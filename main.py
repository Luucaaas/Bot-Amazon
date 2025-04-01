import config
from amazon_bot import AmazonBot
from availability import check_availability
from cart import add_to_cart
from checkout import proceed_to_checkout

# Initialisation du bot
bot = AmazonBot()
bot.open_product_page(config.PRODUCT_URL)

# Vérification du stock et du vendeur
check_availability(bot.driver)  # Le bot quitte déjà si le produit ne convient pas

# Si le produit est en stock et vendu par Amazon, on continue
#add_to_cart(bot.driver)
#proceed_to_checkout(bot.driver)

bot.close_browser()
