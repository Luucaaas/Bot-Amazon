# 🤖 Amazon Auto-Buyer Bot

Ce projet est un **bot automatisé** développé en Python qui permet de :

- Se connecter à un compte Amazon
- Accéder à la page d’un produit
- Vérifier sa disponibilité en stock
- Ajouter l’article au panier en un clic
- Passer la commande automatiquement
- Suivre des **KPIs** (succès, échecs, indisponibilité) via **Google BigQuery**
- Être déployé sous forme de `.exe` pour une exécution facile sur toute machine Windows

---

## 🚀 Technologies utilisées

- 🐍 **Python 3.10+**
- 🧭 **Selenium** : pour contrôler le navigateur web
- 🌐 **Google Cloud Platform (GCP)** : pour stocker les indicateurs via BigQuery
- 📦 **BigQuery** : base de données analytique utilisée pour centraliser les KPIs
- 📸 **Capture automatique d’écran** en cas de crash
- 🪟 **PyInstaller** : pour générer un exécutable `.exe` multiplateforme

---

## ⚙️ Fonctionnalités principales

| Fonction                  | Description |
|--------------------------|-------------|
| Connexion                | Connexion automatique à un compte Amazon |
| Navigation               | Accès direct à une page produit |
| Vérification de stock    | Scraping de la disponibilité produit |
| Achat immédiat           | Ajout au panier via "Acheter maintenant" |
| Skip Amazon Prime        | Contournement des offres Prime |
| Passage à la caisse      | Finalisation de la commande |
| KPI BigQuery             | Envoi de métriques de succès ou d’erreur |
| Screenshot d’erreur      | Capture d’écran si une erreur critique survient |

---

## 💾 Prérequis

- Google Chrome installé
- Compte Amazon valide
- Une clé de service Google (format `.json`) pour accéder à BigQuery
- ChromeDriver correspondant à ta version de Chrome

---

## 🔧 Installation

1. **Télécharger le dossier `dist/`** depuis les [Releases GitHub](#). Il contient :
   - Le fichier exécutable `.exe`
   - Le fichier `produit.txt` (URL du produit Amazon à suivre)
   - Le fichier `config.json` (identifiants Amazon)

2. **Placer votre `clef-service.json`** (Google BigQuery) dans ce même dossier `dist/`

3. Le bot est prêt à être lancé en exécutant simplement le `.exe`.

---

