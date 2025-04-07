import os
from datetime import datetime

def take_screenshot_on_error(driver, folder="screenshots"):
    """Prend une capture d'écran et l'enregistre dans le dossier spécifié."""
    if not os.path.exists(folder):
        os.makedirs(folder)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    screenshot_path = os.path.join(folder, f"error_{timestamp}.png")
    
    try:
        driver.save_screenshot(screenshot_path)
        print(f"📸 Capture d'écran enregistrée : {screenshot_path}")
    except Exception as e:
        print(f"❌ Échec de la capture d'écran : {e}")
