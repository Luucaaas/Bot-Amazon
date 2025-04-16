# 🤖 Amazon Auto-Buyer Bot

Un bot Python intelligent conçu pour **automatiser l'achat d’un produit Amazon** dès qu’il devient disponible. Il est particulièrement utile pour les objets rares, les drops ou les promotions à durée limitée.

---

## 🚀 Fonctionnalités principales

| Fonction                | Description |
|-------------------------|-------------|
| 🔐 Connexion            | Connexion automatique à un compte Amazon |
| 🧭 Navigation           | Accès direct à une page produit via URL |
| 📦 Vérification de stock | Scraping de la disponibilité produit |
| ⚡ Achat immédiat       | Ajout au panier via "Acheter maintenant" |
| ⏩ Skip Amazon Prime    | Contournement des offres Prime forcées |
| 💳 Passage à la caisse  | Finalisation de la commande |
| 📊 KPI BigQuery         | Envoi de métriques (succès, échecs, indisponibilité) |
| 📸 Screenshot d’erreur  | Capture automatique d’écran en cas d’erreur critique |
| ⚙️ Multi-machine        | Centralisation des KPIs pour plusieurs comptes |
| 🧩 Configuration simple | Fichier `config.json` modifiable facilement |

---

## 🧰 Technologies utilisées

- 🐍 Python 3.10+
- 🧭 [Selenium](https://www.selenium.dev/) – Automatisation du navigateur
- 🌐 [Google Cloud BigQuery](https://cloud.google.com/bigquery) – Stockage des KPIs
- 🪟 [PyInstaller](https://pyinstaller.org/) – Génération de l’exécutable `.exe`
- 📸 `Pillow` – Pour les captures d’écran
- 📦 `tzdata` – Gestion des fuseaux horaires

---

## 📁 Structure du projet

src:
  main.py: file
  bot.py: file
  availability.py: file
  config.py: file
  kpi.py: file
  assets:
    config.json: file
    product_url.txt: file


---

## 💾 Prérequis

- ✅ Google Chrome installé
- ✅ Un compte Amazon actif
- ✅ Une clé de service Google (fichier `.json`) pour BigQuery
- ✅ ChromeDriver correspondant à la version de Chrome installée

---

## 🔧 Installation

1. Télécharger le dossier `dist/` depuis la section [📦 Releases](https://github.com/Luucaaas/Bot-Amazon/releases/tag/v1.0.0) 
2. Placer les fichiers suivants dans ce dossier :
   - `bot.exe` : le fichier exécutable
   - `assets/config.json` : identifiants Amazon
   - `assets/product_url.txt` : lien du produit Amazon à suivre
   - `assets/key-service.json` : ta clé d’authentification Google Cloud

3. Double-cliquer sur le `.exe` : le bot se lance automatiquement.

---

## 🛡️ Sécurité & limitations

> ⚠️ **Ce projet est un outil d’automatisation à usage personnel.** Son utilisation doit rester conforme aux conditions d'utilisation d'Amazon.  
> ❗ Un usage excessif peut entraîner un blocage temporaire ou permanent du compte Amazon.

---

## 🎥 Démo (optionnelle)

Ajoute ici un GIF ou un lien vers une vidéo YouTube :

> 📽️ *[Lien vers la démo ici]*

---

## 👨‍💻 Auteur

Développé par **Lucas Leclercq**  
📧 luc.lec38@gmail.com  
🔗 [LinkedIn](https://www.linkedin.com/in/ton-profil)

-------------------------------------------------------------------------------------------------------------------------------


# 🤖 Amazon Auto-Buyer Bot

An intelligent Python bot designed to **automate the purchase of an Amazon product** as soon as it becomes available. Perfect for limited-stock items, drops, or flash sales.

---

## 🚀 Key Features

| Feature                  | Description |
|--------------------------|-------------|
| 🔐 Login                | Automatically logs into an Amazon account |
| 🧭 Navigation           | Directly opens a product page via URL |
| 📦 Stock Check         | Scrapes product availability |
| ⚡ One-Click Purchase   | Adds to cart via "Buy Now" |
| ⏩ Skip Prime Offers    | Skips forced Amazon Prime upsell |
| 💳 Checkout            | Automatically completes the purchase |
| 📊 BigQuery KPIs       | Sends success/error/unavailable metrics |
| 📸 Error Screenshot    | Captures screenshots on critical errors |
| ⚙️ Multi-machine Ready | KPI tracking across multiple machines/accounts |
| 🧩 Easy Setup          | Editable `config.json` configuration file |

---

## 🧰 Tech Stack

- 🐍 Python 3.10+
- 🧭 [Selenium](https://www.selenium.dev/) – Web automation
- 🌐 [Google BigQuery](https://cloud.google.com/bigquery) – Stores KPIs
- 🪟 [PyInstaller](https://pyinstaller.org/) – Builds cross-platform `.exe`
- 📸 `Pillow` – Screenshot capture
- 📦 `tzdata` – Timezone management

---

## 📁 Project Structure

src:
  main.py: file
  bot.py: file
  availability.py: file
  config.py: file
  kpi.py: file
  assets:
    config.json: file
    product_url.txt: file


---

## 💾 Requirements

- ✅ Google Chrome installed
- ✅ Valid Amazon account
- ✅ Google service account key (`.json`) for BigQuery
- ✅ ChromeDriver matching your local Chrome version

---

## 🔧 Installation

1. Download the `dist/` folder from the [📦 Releases](https://github.com/Luucaaas/Bot-Amazon/releases/tag/v1.0.0).
2. Place the following files into that folder:
   - `bot.exe` : executable file
   - `assets/config.json` : your Amazon credentials
   - `assets/product_url.txt` : product link to monitor
   - `assets/key-service.json` : Google Cloud authentication key

3. Double-click the `.exe` file — the bot starts instantly.

---

## 🛡️ Disclaimer

> ⚠️ **This project is for personal automation purposes only.**  
> Please ensure your usage complies with Amazon’s Terms of Service.  
> ❗ Excessive or abusive use may result in temporary or permanent account suspension.

---


## 👨‍💻 Author

Developed by **Lucas Leclercq**  
📧 luc.lec38@gmail.com  
🔗 [LinkedIn](https://www.linkedin.com/in/your-profile)

---


