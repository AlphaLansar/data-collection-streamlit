# Data Collection & Analytics Platform

## Projet d'examen — Data Collection, Web Scraping, Cleaning & Streamlit Deployment

**Auteur : Alpha Abdoulaye Lansar**  
**Master Intelligence Artificielle**  

Projet réalisé dans le cadre du module **Data Collection**.

---

# 1. Présentation du projet

Ce projet consiste à concevoir une plateforme complète de collecte, traitement, stockage et visualisation de données issues du web.

L'objectif est de mettre en place une chaîne complète de traitement des données :

```
Web Sources
     |
     ↓
Web Scraping Selenium
     |
     ↓
Nettoyage et préparation des données
     |
     ↓
Stockage SQL SQLite
     |
     ↓
Analyse exploratoire
     |
     ↓
Dashboard interactif Streamlit
     |
     ↓
Evaluation utilisateur
```

L'application permet :

- de scraper automatiquement des données web ;
- de nettoyer et transformer les données collectées ;
- de stocker les données dans une base SQL ;
- d'explorer les résultats via des dashboards interactifs ;
- de télécharger les datasets ;
- d'évaluer l'application grâce aux formulaires Google Forms et KoboToolbox.

---

# 2. Sources de données

Deux sources de données ont été utilisées conformément aux consignes du projet.

---

## Source 1 — Books To Scrape

URL :

```
https://books.toscrape.com/catalogue/page-1.html
```

### Pagination

Scraping réalisé sur plusieurs pages du catalogue.

### Variables collectées

| Variable | Description |
|---|---|
| title | Titre du livre |
| price | Prix |
| availability | Disponibilité |
| products_count | Nombre de produits par page |
| rating | Note du produit |
| reviews | Nombre de reviews |
| description | Description |
| product_type | Catégorie du produit |
| tax | Taxe |

---

## Source 2 — Gaaraas Cars

URL :

```
https://www.gaaraas.com/fr/users/dakar-auto?page=1
```

### Pagination

Collecte réalisée sur plusieurs pages d'annonces automobiles.

### Variables collectées

| Variable | Description |
|---|---|
| brand | Marque |
| model | Modèle |
| year | Année |
| price | Prix |
| mileage | Kilométrage |
| transmission | Type de boîte |
| region | Région de vente |

---

# 3. Technologies utilisées

## Langages

- Python

## Data Collection

- Selenium WebDriver

## Data Processing

- Pandas
- NumPy

## Database

- SQLite
- SQLAlchemy

## Visualisation

- Streamlit
- Matplotlib
- Plotly

## Versioning

- Git
- GitHub

---

# 4. Architecture du projet

```
exam-data-collection-final/

│
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
│   ├── cleaned/
│   └── nocode/
│
├── reports/
│   ├── figures/
│   └── statistics/
│
├── streamlit_app/
│   ├── Home.py
│   └── pages/
│       ├── 1_Scraping.py
│       ├── Books_Dashboard.py
│       ├── Cars_Dashboard.py
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

# 6. Création de l'environnement virtuel

Créer l'environnement :

```bash
python3 -m venv .venv
```

Activer :

Linux :

```bash
source .venv/bin/activate
```

---

# 7. Installation des dépendances

```bash
pip install -r requirements.txt
```

---

# 8. Scraping avec Selenium

## Books To Scrape

Exemple :

```bash
python scraper/books_scraper.py --pages 5
```

Résultat :

```
data/raw/books.csv
```

---

## Gaaraas Cars

Exemple :

```bash
python scraper/cars_scraper.py --pages 5
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

Résultat :

```
data/cleaned/books_clean.csv
```

---

## Cars

```bash
python cleaning/clean_cars.py
```

Résultat :

```
data/cleaned/cars_clean.csv
```

---

# 10. Base de données SQL

La base utilisée est SQLite.

Création et import :

## Books

```bash
python -m database.import_books
```

## Cars

```bash
python -m database.import_cars
```

Base générée :

```
books_cars.db
```

Tables :

- books
- cars

---

# 11. Application Streamlit

Lancer l'application :

```bash
streamlit run streamlit_app/Home.py
```

L'application contient :

## Module Scraping

Permet :

- lancer la collecte Selenium ;
- choisir la source ;
- choisir le nombre de pages.

---

## Module Download

Permet :

- télécharger les données brutes Selenium ;
- télécharger les données nettoyées ;
- télécharger les données issues du scraping no-code Web Scraper.

---

## Dashboards

### Books Dashboard

Fonctionnalités :

- statistiques générales ;
- analyse des prix ;
- distribution des notes ;
- catégories ;
- filtres interactifs.

---

### Cars Dashboard

Fonctionnalités :

- statistiques automobiles ;
- analyse des prix ;
- marques populaires ;
- kilométrage ;
- transmission ;
- filtres dynamiques.

---

## Module Evaluation

Accès aux formulaires :

- Google Forms ;
- KoboToolbox.

---

# 12. Scraping No-Code

Une seconde collecte est réalisée avec l'extension Chrome :

```
Web Scraper
```

Les fichiers bruts seront stockés dans :

```
data/nocode/
```

Structure prévue :

```
data/nocode/

├── books_webscraper_raw.csv

└── cars_webscraper_raw.csv
```

---

# 13. Nettoyage appliqué

Les traitements réalisés :

- suppression des valeurs manquantes ;
- conversion des types numériques ;
- nettoyage des prix ;
- nettoyage du kilométrage ;
- traitement des doublons ;
- standardisation des colonnes.

---

# 14. Résultats

La plateforme permet :

- une collecte automatisée ;
- une préparation complète des données ;
- une visualisation interactive ;
- un stockage structuré ;
- une évaluation utilisateur.

---

# 15. Déploiement

Application Streamlit :

Lien :

```
À compléter après déploiement
```

Repository GitHub :

```
https://github.com/AlphaLansar/data-collection-streamlit
```

---

# 16. Vidéo de présentation

Structure :

## Partie 1 — Explication du code (8 minutes)

Présentation :

- architecture du projet ;
- scraping Selenium ;
- nettoyage ;
- base SQL ;
- dashboards.

## Partie 2 — Démonstration application (2 minutes)

Présentation :

- lancement scraping ;
- visualisation dashboard ;
- téléchargement ;
- formulaires d'évaluation.

---

# 17. Auteur

## Alpha Abdoulaye Lansar

Master Intelligence Artificielle

Domaines d'intérêt :

- Artificial Intelligence
- Data Science
- Robotics
- Edge AI
- Intelligent Systems

---

# Conclusion

Ce projet met en œuvre une chaîne complète de collecte et exploitation de données :

**Collect → Clean → Store → Analyze → Visualize → Evaluate**

Il constitue une base pour le développement de solutions intelligentes orientées données.
