import streamlit as st


st.set_page_config(
    page_title="Data Collection Platform",
    page_icon="📊",
    layout="wide"
)


# =====================================================
# HEADER
# =====================================================

st.title(
    "Data Collection & Analytics Platform"
)


st.markdown(
"""
### Projet Data Collection

Application développée dans le cadre du Master Intelligence Artificielle.

Cette plateforme présente une chaîne complète de traitement
des données :

**Collecte Web → Nettoyage → Stockage SQL → Analyse → Visualisation**
"""
)



st.divider()



# =====================================================
# PRESENTATION
# =====================================================

st.header(
    "Présentation du projet"
)


st.write(
"""
L'objectif de ce projet est de concevoir une application permettant
la collecte automatique de données provenant de sources web,
leur préparation pour l'analyse et leur exploration interactive.

Deux sources de données sont utilisées :

- Books To Scrape : catalogue de livres
- Gaaraas : annonces automobiles Dakar
"""
)



st.divider()



# =====================================================
# PIPELINE
# =====================================================

st.header(
    "Architecture du pipeline"
)


col1, col2, col3, col4 = st.columns(4)



with col1:

    st.subheader(
        "1. Collecte"
    )

    st.write(
"""
Technologie :

Selenium WebDriver

Extraction automatique depuis :

- Books To Scrape
- Gaaraas Cars
"""
)



with col2:

    st.subheader(
        "2. Préparation"
    )

    st.write(
"""
Nettoyage avec Pandas :

- traitement valeurs manquantes
- conversion des formats
- suppression doublons
- préparation analytique
"""
)



with col3:

    st.subheader(
        "3. Stockage"
    )

    st.write(
"""
Base de données :

SQLite

ORM :

SQLAlchemy

Tables :

- books
- cars
"""
)



with col4:

    st.subheader(
        "4. Analyse"
    )

    st.write(
"""
Exploration avec Streamlit :

- indicateurs
- graphiques
- filtres
- export CSV
"""
)



st.divider()



# =====================================================
# SOURCES
# =====================================================

st.header(
    "Sources de données"
)



col1, col2 = st.columns(2)



with col1:

    st.subheader(
        "Books To Scrape"
    )


    st.write(
"""
Variables collectées :

- Titre du livre
- Prix
- Disponibilité
- Nombre de produits
- Note
- Nombre de reviews
- Description
- Catégorie
- Taxe
"""
)



with col2:

    st.subheader(
        "Gaaraas Cars"
    )


    st.write(
"""
Variables collectées :

- Marque
- Modèle
- Année
- Prix
- Kilométrage
- Type de transmission
- Région de vente
"""
)



st.divider()



# =====================================================
# TECHNOLOGIES
# =====================================================

st.header(
    "Technologies utilisées"
)


st.code(
"""
Python
Selenium WebDriver
Pandas
SQLAlchemy
SQLite
Streamlit
Matplotlib
Plotly
Git / GitHub
"""
)



st.divider()



# =====================================================
# AUTEUR
# =====================================================

st.header(
    "Auteur"
)


st.write(
"""
**Alpha Abdoulaye Lansar**

Master Intelligence Artificielle

Projet :
Data Collection — Web Scraping, Data Cleaning,
Database Integration and Streamlit Deployment
"""
)



st.caption(
"""
Pipeline conçu et développé personnellement dans un objectif
d'application des méthodes Data Engineering et Artificial Intelligence.
"""
)