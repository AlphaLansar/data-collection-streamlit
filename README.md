# Data Collection & Analytics Platform

## Projet d'examen — Data Collection, Web Scraping, Cleaning & Streamlit Deployment

**Auteur : Alpha Abdoulaye Lansar**  
**Formation : Master Intelligence Artificielle**

Projet réalisé dans le cadre du module **Data Collection**.

---

# 1. Présentation du projet

Ce projet consiste à développer une plateforme complète de collecte, nettoyage, stockage et visualisation de données web.

L'objectif est de construire une chaîne complète :

```
Sources Web
     |
     ↓
Scraping Selenium
     |
     ↓
Nettoyage Pandas
     |
     ↓
Base SQLite
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

- la collecte automatique de données web ;
- le nettoyage et la transformation des données ;
- le stockage dans une base SQL ;
- l'analyse exploratoire ;
- la visualisation interactive ;
- l'export des datasets ;
- l'évaluation utilisateur.

---

# 2. Sources de données

Deux sources ont été utilisées.

---

# Source 1 : Books To Scrape

URL :

```
https://books.toscrape.com/catalogue/page-1.html
```

## Méthode

Scraping réalisé avec :

- Selenium WebDriver
- Pagination automatique

## Variables collectées

| Variable | Description |
|-|-|
| title | Titre du livre |
| price | Prix |
| availability | Disponibilité |
| products_count | Nombre de produits |
| rating | Note |
| reviews | Nombre de reviews |
| description | Description |
| product_type | Catégorie |
| tax | Taxe |

Dataset obtenu :

```
1000 livres
```

---

# Source 2 : Gaaraas Dakar Auto

URL :

```
https://www.gaaraas.com/fr/users/dakar-auto?page=1
```

## Méthode

Scraping avec Selenium sur les annonces automobiles.

## Variables collectées

| Variable | Description |
|-|-|
| brand | Marque |
| model | Modèle |
| year | Année |
| price | Prix |
| mileage | Kilométrage |
| transmission | Boîte de vitesse |
| region | Région |

Dataset obtenu :

```
245 véhicules
```

---

# 3. Technologies utilisées

## Langage

- Python

## Web Scraping

- Selenium WebDriver

## Nettoyage

- Pandas
- NumPy

## Base de données

- SQLite
- SQLAlchemy

## Visualisation

- Streamlit
- Plotly
- Matplotlib

## No-Code Scraping

- Web Scraper Chrome Extension

## Versioning

- Git
- GitHub

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
│   ├── cleaned/
│   └── nocode/
│
├── reports/
│
├── streamlit_app/
│   ├── Home.py
│   └── pages/
│
├── books_cars.db
│
├── requirements.txt
│
└── README.md
```

---

# 5. Installation

Cloner le projet :

```bash
git clone https://github.com/AlphaLansar/data-collection-streamlit.git
```

Entrer dans le projet :

```bash
cd exam-data-collection-final
```

Créer l'environnement :

```bash
python3 -m venv .venv
```

Activer :

Linux :

```bash
source .venv/bin/activate
```

Installer les dépendances :

```bash
pip install -r requirements.txt
```

---

# 6. Scraping Selenium

## Books

```bash
python scraper/books_scraper.py
```

Résultat :

```
data/raw/books.csv
```

---

## Cars

```bash
python scraper/cars_scraper.py
```

Résultat :

```
data/raw/cars.csv
```

---

# 7. Nettoyage

## Books

```bash
python cleaning/clean_books.py
```

Sortie :

```
data/cleaned/books_clean.csv
```

---

## Cars

```bash
python cleaning/clean_cars.py
```

Sortie :

```
data/cleaned/cars_clean.csv
```

---

# 8. Base de données SQLite

Import Books :

```bash
python -m database.import_books
```

Import Cars :

```bash
python -m database.import_cars
```

Base créée :

```
books_cars.db
```

Tables :

```
books
cars
```

Résultats :

```
Books : 1000 lignes
Cars  : 245 lignes
```

---

# 9. Scraping No-Code

Une deuxième collecte a été réalisée avec :

```
Web Scraper Chrome Extension
```

Objectif :

- collecter les données brutes ;
- conserver les données sans nettoyage ;
- comparer avec la collecte Selenium.

Datasets :

```
data/nocode/books/books.csv

data/nocode/cars/cars.csv
```

---

# 10. Application Streamlit

Lancement local :

```bash
streamlit run streamlit_app/Home.py
```

---

# Modules disponibles

## Scraping

Présentation du pipeline Selenium.

---

## No-Code Web Scraper

Visualisation des données collectées avec l'extension Web Scraper.

---

## Books Dashboard

Analyse :

- prix ;
- disponibilité ;
- notes ;
- catégories ;
- statistiques.

---

## Cars Dashboard

Analyse :

- marques ;
- prix ;
- kilométrage ;
- année ;
- transmission.

---

## Database

Visualisation :

- tables SQLite ;
- statistiques ;
- aperçu SQL.

---

## Download

Téléchargement :

- CSV nettoyés ;
- CSV bruts ;
- base SQLite.

---

## Evaluation

Accès aux formulaires :

- Google Forms
- KoboToolbox

---

# 11. Application déployée

Streamlit Cloud :

https://data-collection-app-drnxvwc4qgjpgmfxacw36y.streamlit.app/

---

# 12. Repository GitHub

https://github.com/AlphaLansar/data-collection-streamlit

---

# 13. Résultats

La plateforme finale permet :

✅ Scraping Selenium  
✅ Scraping No-Code Web Scraper  
✅ Nettoyage automatique  
✅ Base SQL SQLite  
✅ Dashboards interactifs  
✅ Export des données  
✅ Evaluation utilisateur  

---

# 14. Présentation vidéo

Durée : 10 minutes

## Partie 1 — Code (8 minutes)

Présentation :

- architecture ;
- scraping ;
- nettoyage ;
- base SQL ;
- dashboards.

## Partie 2 — Démonstration (2 minutes)

Présentation :

- application Streamlit ;
- visualisation ;
- téléchargement ;
- formulaires.

---

# Auteur

## Alpha Abdoulaye Lansar

Master Intelligence Artificielle

Domaines :

- Artificial Intelligence
- Data Science
- Robotics
- Edge AI
- Intelligent Systems

---

# Conclusion

Ce projet réalise une chaîne complète :

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

Une plateforme complète de collecte et exploitation des données web.