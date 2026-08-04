# Data Collection & Analytics Platform

## Projet d'examen — Web Scraping, Data Cleaning, SQLite Database & Streamlit Dashboard

**Auteur : Alpha Abdoulaye Lansar**
**Formation : Master Intelligence Artificielle**

---

# 1. Présentation du projet

Ce projet consiste à développer une plateforme complète de collecte, traitement, stockage et visualisation de données issues du web.

L'objectif est de construire une chaîne complète de traitement des données :

```
Sources Web
     |
     ↓
Scraping Selenium
     |
     ↓
Nettoyage des données
     |
     ↓
Stockage SQLite
     |
     ↓
Analyse exploratoire
     |
     ↓
Dashboard Streamlit
     |
     ↓
Evaluation utilisateur
```

La plateforme permet :

* la collecte automatique de données web ;
* le nettoyage et la préparation des datasets ;
* le stockage dans une base de données SQL ;
* l'exploration interactive des données ;
* le téléchargement des résultats ;
* l'accès aux formulaires d'évaluation.

---

# 2. Sources de données

Le projet utilise deux sources de données conformément aux exigences de l'examen.

---

# Source 1 — Books To Scrape

URL :

```
https://books.toscrape.com/catalogue/page-1.html
```

Méthode :

```
Selenium WebDriver
```

Variables extraites :

| Variable       | Description                 |
| -------------- | --------------------------- |
| title          | Titre du livre              |
| price          | Prix                        |
| availability   | Disponibilité               |
| products_count | Nombre de produits par page |
| rating         | Note du produit             |
| reviews        | Nombre de reviews           |
| description    | Description                 |
| product_type   | Catégorie                   |
| tax            | Taxe                        |

---

# Source 2 — Gaaraas Dakar Auto

URL :

```
https://www.gaaraas.com/fr/users/dakar-auto?page=1
```

Méthode :

```
Selenium WebDriver
```

Variables extraites :

| Variable     | Description     |
| ------------ | --------------- |
| brand        | Marque          |
| model        | Modèle          |
| year         | Année           |
| price        | Prix            |
| mileage      | Kilométrage     |
| transmission | Type de boîte   |
| region       | Région de vente |

---

# 3. Technologies utilisées

## Langage

* Python

## Web Scraping

* Selenium WebDriver

## Data Processing

* Pandas
* NumPy

## Base de données

* SQLite
* SQLAlchemy

## Visualisation

* Streamlit
* Matplotlib
* Plotly

## Versioning

* Git
* GitHub

## Scraping No-Code

* Web Scraper Chrome Extension

---

# 4. Architecture du projet

```
exam-data-collection-final/

├── scraper/
│   ├── books_scraper.py
│   └── cars_scraper.py
│
├── cleaning/
│   ├── clean_books.py
│   └── clean_cars.py
│
├── analysis/
│   ├── books_analysis.py
│   └── cars_analysis.py
│
├── database/
│   ├── database.py
│   ├── models.py
│   ├── import_books.py
│   └── import_cars.py
│
├── data/
│   ├── raw/
│   │   ├── books.csv
│   │   └── cars.csv
│   │
│   ├── cleaned/
│   │   ├── books_clean.csv
│   │   └── cars_clean.csv
│   │
│   └── nocode/
│
├── reports/
│   ├── figures/
│   └── statistics/
│
├── forms/
│
├── streamlit_app/
│   ├── Home.py
│   └── pages/
│       ├── 1_Scraping.py
│       ├── 2_NoCode_WebScraper.py
│       ├── Books_Dashboard.py
│       ├── Cars_Dashboard.py
│       ├── Database.py
│       ├── Download.py
│       └── Evaluation.py
│
├── requirements.txt
│
└── README.md
```

---

# 5. Installation

## Cloner le projet

```bash
git clone https://github.com/AlphaLansar/data-collection-streamlit.git
```

Entrer dans le dossier :

```bash
cd exam-data-collection-final
```

---

# 6. Environnement virtuel

Création :

```bash
python3 -m venv .venv
```

Activation Linux :

```bash
source .venv/bin/activate
```

---

# 7. Installation des dépendances

```bash
pip install -r requirements.txt
```

---

# 8. Scraping Selenium

## Books

Commande :

```bash
python scraper/books_scraper.py
```

Résultat :

```
data/raw/books.csv
```

---

## Cars

Commande :

```bash
python scraper/cars_scraper.py
```

Résultat :

```
data/raw/cars.csv
```

---

# 9. Nettoyage des données

## Books

```bash
python cleaning/clean_books.py
```

Production :

```
data/cleaned/books_clean.csv
```

---

## Cars

```bash
python cleaning/clean_cars.py
```

Production :

```
data/cleaned/cars_clean.csv
```

---

# 10. Intégration Base de données SQL

La plateforme utilise SQLite.

Création des tables :

```bash
python -m database.import_books
```

```bash
python -m database.import_cars
```

Base générée :

```
books_cars.db
```

Tables disponibles :

```
books
cars
```

Vérification :

```sql
SELECT name FROM sqlite_master WHERE type='table';
```

---

# 11. Application Streamlit

Lancement :

```bash
streamlit run streamlit_app/Home.py
```

---

# 12. Modules de l'application

## Web Scraping Pipeline

Cette page présente :

* les datasets collectés ;
* l'état des fichiers ;
* l'architecture du pipeline.

---

## No-Code Web Scraper

Cette partie correspond à la contrainte examen :

Outil utilisé :

```
Web Scraper Chrome Extension
```

Objectif :

* collecter des données brutes ;
* exporter les fichiers CSV ;
* présenter les résultats sans nettoyage.

Les fichiers sont stockés dans :

```
data/nocode/
```

---

## Books Dashboard

Fonctionnalités :

* nombre total de livres ;
* prix moyen ;
* distribution des prix ;
* analyse des notes ;
* exploration des catégories ;
* visualisation interactive.

---

## Cars Dashboard

Fonctionnalités :

* nombre de véhicules ;
* prix moyen ;
* marques disponibles ;
* kilométrage ;
* transmission ;
* analyse des années ;
* filtres interactifs.

---

## Database Explorer

Cette interface permet :

* connexion SQLite ;
* visualisation des tables ;
* aperçu SQL ;
* statistiques des données.

Pipeline présenté :

```
Scraping
↓
Cleaning
↓
SQLite
↓
Dashboard
```

---

## Download Center

Permet le téléchargement :

* datasets nettoyés CSV ;
* datasets bruts ;
* base SQLite.

---

## Evaluation

Accès aux formulaires :

* Google Forms ;
* KoboToolbox.

---

# 13. Traitement des données

Les opérations réalisées :

* suppression des valeurs manquantes ;
* conversion des types ;
* nettoyage des prix ;
* nettoyage du kilométrage ;
* traitement des doublons ;
* standardisation des colonnes.

---

# 14. Résultats obtenus

La plateforme finale permet :

✓ collecte automatique avec Selenium
✓ scraping No-Code avec Web Scraper
✓ nettoyage des données
✓ stockage SQL SQLite
✓ analyse exploratoire
✓ dashboards interactifs
✓ export des données
✓ évaluation utilisateur

---

# 15. Déploiement

Application Streamlit :

```
Lien à compléter
```

Repository GitHub :

```
Lien à compléter
```

---

# 16. Présentation vidéo

Durée prévue : 10 minutes

## Partie 1 — Explication du code (8 minutes)

Présentation :

* architecture ;
* scraping Selenium ;
* nettoyage ;
* base SQL ;
* dashboards.

## Partie 2 — Démonstration (2 minutes)

Présentation :

* lancement application ;
* dashboards ;
* téléchargement ;
* formulaires.

---

# 17. Auteur

## Alpha Abdoulaye Lansar

Master Intelligence Artificielle

Domaines :

* Artificial Intelligence
* Data Science
* Robotics
* Edge AI
* Intelligent Systems

---

# Conclusion

Ce projet met en œuvre une chaîne complète de valorisation des données :

```
Collect
   ↓
Clean
   ↓
Store
   ↓
Analyze
   ↓
Visualize
   ↓
Evaluate
```

Il représente une application complète de Data Collection combinant Web Scraping, Data Engineering et Data Visualization.
