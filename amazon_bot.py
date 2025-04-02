from selenium import webdriver
import config

class AmazonBot:
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")  # Mode sans interface (optionnel)
        self.driver = webdriver.Chrome(options=options)

    def open_product_page(self, url):
        """Ouvre la page produit."""
        self.driver.get(url)
        print("Page produit ouverte.")

    def close_browser(self):
        """Ferme le navigateur proprement."""
        self.driver.quit()
