# 🤖 Bot Amazon – Achat automatique intelligent

Un bot Python intelligent conçu pour **automatiser l'achat d’un produit Amazon** dès qu’il devient disponible. Il est particulièrement utile pour les objets rares, les drops ou les promotions à durée limitée.

---

## ✨ À propos du projet

🎓 8 mois se sont écoulés depuis la fin de mon alternance.  
8 mois de recherches d'emploi, d'envois de candidatures, de suivis d’e-learnings, de certifications, et de tentatives pour faire ressortir ma valeur sur un CV.

Et puis il y a 2 mois, une idée a émergé d'une simple discussion.  
Un ami me partageait le temps qu’il passait sur Amazon à essayer d’acheter des produits biens spécifiques… et rarement en stock.

💡 Ma solution : créer un bot capable d’acheter automatiquement un article dès qu’il est remis en stock sur Amazon.

Je ne suis "que" Data Analyst Junior, mais j’ai relevé le défi.  
Pour apprendre. Pour me challenger.  
Et surtout, pour prouver aux recruteurs que j’ai ma place dans une entreprise.

🚀 Après 1 mois et demi de conception, voici le projet final :  
Un robot alimenté par une simple URL, qui surveille Amazon en temps réel pour détecter l’article rare… et passer commande dès qu’il est dispo.

🧠 Techniquement :
- 100 % Python
- Navigation automatisée avec Selenium
- KPI de succès, d’échecs, et d’indisponibilité envoyés vers BigQuery (GCP)
- Dashboard d’analyse pour suivre les performances (eh oui, je reste Data Analyst avant tout !)

📁 Le tout packagé dans un exécutable simple à utiliser, même sans connaissance technique.

✅ En un mois, j’ai livré un outil complet, qui répond parfaitement au cahier des charges.  
Et ce n’est que le début… je continue à l’améliorer et à monter en compétences.

🧪 Vous voulez tester ? Le robot est dispo juste ici 👇  
🔗 [📦 Releases](https://github.com/Luucaaas/Bot-Amazon/releases/tag/v1.0.0)

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

## ⚙️ Fonctionnement

- Le robot se connecte à Amazon avec les identifiants fournis dans config.json. ⚠️ Un captcha peut apparaître au lancement : il doit être complété manuellement.
- Il se rend sur la page du produit spécifiée dans product_url.txt.
- Il vérifie que l'article soit en stock, vendu et expédié par Amazon.
- Si ces conditions ne sont pas remplies, il rafraîchit la page autant de fois que défini dans config.json.
- Si les conditions sont remplies, il clique sur "Acheter cet article" puis sur "Valider votre paiement", et se ferme automatiquement.
- Si les conditions ne sont toujours pas remplies après le nombre maximal de rafraîchissements, le robot se ferme proprement.

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
  - main.py: file
  - amazon_bot.py: file
  - availability.py: file
  - config.py: file
  - checkout.py file
  - prime.py file
  - screenshot.py
  - cart.py: file
  - get_product.py: file
  - ident.py: file
  - kpi.py: file
  - assets:
      - config.json: file
      - product_url.txt: file
      - key.json: file

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
   - `config.json` : identifiants Amazon et nombre de refresh souhaité
   - `product_url.txt` : lien du produit Amazon à suivre
   - `key.json` : ta clé d’authentification Google Cloud

3. Double-cliquer sur le `.exe` : le bot se lance automatiquement.

---

## 🧪 Lancer depuis le code source

1. Cloner le repo :

git clone https://github.com/Luucaaas/Bot-Amazon.git
cd Bot-Amazon
pip install -r requirements.txt
python src/main.py

--

## 🛡️ Sécurité & limitations

> ⚠️ **Ce projet est un outil d’automatisation à usage personnel.** Son utilisation doit rester conforme aux conditions d'utilisation d'Amazon.  
> ❗ Un usage excessif peut entraîner un blocage temporaire ou permanent du compte Amazon.

---

## 👨‍💻 Auteur

Développé par **Lucas Leclercq**  
📧 luc.lec38@gmail.com  
🔗 [LinkedIn](www.linkedin.com/in/lucasleclercq1)

-------------------------------------------------------------------------------------------------------------------------------


# 🤖 Amazon Bot – Smart Auto-Purchase

A smart Python bot designed to **automatically buy an Amazon product** as soon as it becomes available.  
Perfect for limited drops, rare items, or short-lived promotions.

---

## ✨ About the project

🎓 8 months have passed since the end of my work-study program.  
8 months of job applications, online certifications, personal projects, and trying to prove my worth on a CV.

Then 2 months ago, an idea came out of a casual conversation.  
A friend shared how much time he was spending on Amazon trying to buy a rare item that kept going out of stock.

💡 My solution: Build a bot that automatically buys the item as soon as it's back in stock.

I’m “just” a Junior Data Analyst, but I took the challenge.  
To learn. To push myself.  
And most of all, to show recruiters that I deserve a place in their team.

🚀 After 6 weeks of research and development, here is the final product:  
A bot that takes a simple URL, monitors Amazon in real time, and places an order instantly when the item is back.

🧠 Tech-wise:
- 100% Python
- Automated browser with Selenium
- Success/failure/unavailable KPIs sent to BigQuery (GCP)
- Analytics dashboard to track performance (still a Data Analyst at heart!)

📁 The tool is packaged as a simple `.exe` to run, no technical skills needed.

✅ In one month, I delivered a complete product that meets every requirement.  
This is only the beginning… I'm still improving and learning every day.

🧪 Want to try it? The bot is available here 👇
🔗 [📦 Releases](https://github.com/Luucaaas/Bot-Amazon/releases/tag/v1.0.0)

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

## ⚙️ How It Works

- The bot logs into Amazon using the credentials provided in config.json. ⚠️ A captcha may appear at launch and must be solved manually.
- It navigates to the product page specified in product_url.txt.
- It checks if the item is in stock, and sold and shipped by Amazon.
- If the conditions are not met, the bot refreshes the page as many times as specified in config.json.
- If the conditions are met, the bot clicks "Buy Now", then "Place your order", and shuts down automatically.
- If the item remains unavailable after all refresh attempts, the bot exits cleanly.

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
  - main.py: file
  - amazon_bot.py: file
  - availability.py: file
  - config.py: file
  - checkout.py file
  - prime.py file
  - screenshot.py
  - cart.py: file
  - get_product.py: file
  - ident.py: file
  - kpi.py: file
  - assets:
      - config.json: file
      - product_url.txt: file
      - key.json: file


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
   - `config.json` : your Amazon credentials
   - `product_url.txt` : product link to monitor
   - `key.json` : Google Cloud authentication key

3. Double-click the `.exe` file — the bot starts instantly.

---

## 🧪 Running from Source

1. Clone the repository:

git clone https://github.com/Luucaaas/Bot-Amazon.git
cd Bot-Amazon
pip install -r requirements.txt
python src/main.py

--

## 🛡️ Disclaimer

> ⚠️ **This project is for personal automation purposes only.**  
> Please ensure your usage complies with Amazon’s Terms of Service.  
> ❗ Excessive or abusive use may result in temporary or permanent account suspension.

---


## 👨‍💻 Author

Developed by **Lucas Leclercq**  
📧 luc.lec38@gmail.com  
🔗 [LinkedIn](www.linkedin.com/in/lucasleclercq1)

---


