from selenium import webdriver
import config as config

class AmazonBot:
    def __init__(self):
        options = webdriver.ChromeOptions()
        #options.add_argument("--headless")  # Mode sans interface
        self.driver = webdriver.Chrome(options=options)

    def open_product_page(self, url):
        """Ouvre la page produit."""
        self.driver.get(url)
        print(f"Opening URL: {url}")
        print("Page produit ouverte.")

    def close_browser(self):
        """Ferme le navigateur proprement."""
        self.driver.quit()
