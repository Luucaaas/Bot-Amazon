import config
import get_product
from config import EMAIL, PASSWORD
from amazon_bot import AmazonBot
from availability import check_availability
from cart import buy_now
from ident import login_amazon
from prime import skip_prime_offer
from checkout import proceed_to_checkout
from screenshot import take_screenshot_on_error  
import sys
import traceback


def main():
    bot = None
    try:
        print("\U0001f512 Initialisation du bot Amazon...")
        bot = AmazonBot()

        login_amazon(bot.driver, EMAIL, PASSWORD)

        PRODUCT_URL = get_product.get_product_url()
        bot.open_product_page(PRODUCT_URL)

        check_availability(bot.driver)  

        buy_now(bot.driver)

        skip_prime_offer(bot.driver)

        proceed_to_checkout(bot.driver)

    except Exception as e:
        print("\n❌ Une erreur inattendue est survenue :", str(e))
        traceback.print_exc()
        if bot:
            take_screenshot_on_error(bot.driver)
            bot.close_browser()
        sys.exit(1)

    print("\n🎉 Bot exécuté avec succès !")


if __name__ == "__main__":
    main()
