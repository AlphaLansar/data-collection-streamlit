Tu es mon assistant technique pour terminer mon projet d'examen Master IA :
"Data Collection — Web scraping, nettoyage de données et déploiement d'une application Streamlit".

IMPORTANT :

- Ne me donne pas de longues discussions inutiles.
- Je veux avancer étape par étape jusqu'à la livraison finale.
- Toujours donner des commandes terminal exactes.
- Toujours donner les chemins exacts des fichiers.
- Quand un fichier doit être modifié, donner le code COMPLET du fichier, pas des morceaux.
- Après chaque étape, attendre mon retour avant de continuer.
- Si une erreur apparaît, on la corrige avant de passer à l'étape suivante.
- Ne jamais casser ce qui fonctionne déjà.
- Pas d'emojis dans le travail.
- Objectif : projet professionnel prêt pour GitHub, vidéo de démonstration et dépôt final.

==============================
CONTEXTE DU PROJET
==================

Projet :
Data Collection — Web scraping, nettoyage de données et déploiement Streamlit.

Critères du professeur :

1) Sources de données

SOURCE 1 :
Books to Scrape
https://books.toscrape.com/catalogue/page-1.html

Pagination :
Toutes les pages du catalogue.

Variables demandées :

- Titre du livre
- Prix
- Disponibilité
- Nombre de produits
- Note
- Nombre de reviews
- Description
- Type produit
- Tax

SOURCE 2 :
Gaaraas Dakar Auto
https://www.gaaraas.com/fr/users/dakar-auto?page=1

Pagination :
100 pages.

Variables demandées :

- Marque
- Modèle
- Année
- Prix
- Kilométrage
- Type boîte
- Région vente

==============================
CONTRAINTES PROF
================

Scraping coding :

- Selenium obligatoire.
- BeautifulSoup interdit.

Scraping no-code :

- Web Scraper Chrome extension.
- Données brutes non nettoyées.

Application Streamlit :
Elle doit permettre :

Scraper des données depuis plusieurs pages.

L'utilisateur doit pouvoir choisir :

- source Books ou Cars
- nombre de pages à scraper

Télécharger les données brutes issues du scraping no-code.

Dashboard des données nettoyées :

- Books Dashboard
- Cars Dashboard

Accéder aux formulaires d'évaluation :

- Kobo Form
- Google Form

Base SQL :

- Une base SQL liée à l'application.
- Une table par source.

Formulaires :

- Kobo
- Google Forms
- accessibles depuis Streamlit.

==============================
ETAT ACTUEL DU PROJET
=====================

Machine :
Ubuntu 22.04
Dell XPS 15 9570

Projet :

~/Documents/exam-data-collection-final

Environnement :

.venv activé.

Structure actuelle :

exam-data-collection-final

├── analysis
│   ├── books_analysis.py
│   ├── cars_analysis.py
│   └── check_raw_data.py

├── cleaning
│   ├── clean_books.py
│   └── clean_cars.py

├── data
│   ├── raw
│   │   ├── books.csv
│   │   └── cars.csv
│   │
│   └── cleaned
│       ├── books_clean.csv
│       └── cars_clean.csv

├── database
│   ├── database.py
│   ├── models.py
│   ├── import_books.py
│   ├── import_cars.py
│   ├── check_books.py
│   ├── check_cars.py
│   └── __init__.py

├── reports
│   ├── books
│   │   ├── figures
│   │   └── statistics
│   │
│   └── cars
│       ├── figures
│       └── statistics

├── scraper
│   ├── books_scraper.py
│   └── cars_scraper.py

├── streamlit_app
│   ├── Home.py
│   └── pages
│       ├── Books_Dashboard.py
│       ├── Cars_Dashboard.py
│       ├── Download.py
│       └── Evaluation.py

==============================
CE QUI EST DEJA TERMINE
=======================

1) Scraping Books Selenium :
   Fonctionne.

Ancien résultat :
999 livres.

2) Nettoyage Books :
   Fonctionne.

books_clean.csv existe.

3) Base SQL Books :
   Fonctionne.

Test :

python -c "from sqlalchemy import create_engine, inspect; engine=create_engine('sqlite:///books.db'); print(inspect(engine).get_table_names())"

Résultat :

['books']

4) Scraping Cars :
   Fonctionne dans une ancienne version.

Résultat obtenu :
245 voitures.

cars_clean.csv existe.

Colonnes :

url
title
location
price
mileage
year
color
body_type
fuel
transmission
engine
air_conditioning
steering
condition
status
created_date
description

5) Nettoyage Cars :
   Fonctionne.

Résultat :

245 lignes.

6) Analyse Books :
   Terminé.

Créé :

reports/books/figures

- books_availability.png
- books_price_distribution.png
- books_price_rating.png
- books_rating_distribution.png
- books_top_expensive.png

7) Analyse Cars :
   Terminé.

Créé :

reports/cars/figures

- car_brands.png
- car_fuel.png
- car_price_distribution.png
- car_price_fuel.png
- car_year_price.png

8) Dashboard Streamlit :

Lancé avec :

streamlit run streamlit_app/Home.py

Fonctionne :

- Books Dashboard
- Cars Dashboard

Problèmes restants :

- bouton Download à améliorer
- Evaluation page à connecter

==============================
POINT EXACT OU ON S'EST ARRETE
==============================

On travaille actuellement sur :

scraper/cars_scraper.py

La première version avait collecté 245 voitures.

Une nouvelle version plus lente a été testée.

Le dernier code donné doit être vérifié.

Commande de test :

python scraper/cars_scraper.py --pages 1

Objectif :
avoir :

Scraping page 1

Annonces trouvées: ...

Puis :

CSV créé

Nombre voitures: ...

==============================
OBJECTIF FINAL RESTANT
======================

Terminer rapidement :

ETAPE 1 :
Valider cars_scraper.py

ETAPE 2 :
Améliorer Home.py Streamlit :

L'application finale doit avoir :

Accueil

Choix :

1 - Scraper Books
2 - Scraper Cars

Input :
Nombre de pages

Bouton :
Lancer scraping

Afficher :
progression

Sauvegarder CSV

ETAPE 3 :
Dashboard professionnel :

Books :

- KPIs
- filtres
- graphiques Plotly interactifs
- tableau
- téléchargement

Cars :

- KPIs
- filtres
- prix
- carburant
- année
- kilométrage
- graphiques Plotly interactifs
- tableau
- téléchargement

ETAPE 4 :
Download Page :

Permettre :

Télécharger :

- raw books.csv
- raw cars.csv
- cleaned books_clean.csv
- cleaned cars_clean.csv

ETAPE 5 :
Evaluation Page :

Créer liens :

Google Form
Kobo Form

ETAPE 6 :
README professionnel :

README.md doit contenir :

- contexte
- objectifs
- architecture
- technologies
- installation
- utilisation
- screenshots
- résultats
- limites
- perspectives

ETAPE 7 :
Préparation vidéo 10 minutes :

8 minutes :
explication code

2 minutes :
démonstration application

==============================
METHODE DE TRAVAIL
==================

Toujours travailler ainsi :

Analyser l'état actuel.

Donner UNE seule étape.

Donner commandes exactes.

Donner fichiers complets si modification.

Attendre mon retour.

Reprends maintenant exactement où nous sommes arrêtés :
validation de scraper/cars_scraper.py puis finalisation Streamlit selon les critères du professeur.
