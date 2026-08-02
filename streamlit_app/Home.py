import streamlit as st



st.set_page_config(
    page_title="Data Collection Platform",
    layout="wide"
)



# =====================================================
# HEADER
# =====================================================


st.title(
    "Data Collection & Analytics Platform"
)



st.write(
"""
Plateforme de collecte, traitement et analyse de données
développée dans le cadre du projet Data Collection.

L'objectif est de mettre en place une chaîne complète
de traitement des données allant de l'extraction web
jusqu'à la visualisation interactive.
"""
)



st.divider()



# =====================================================
# OBJECTIFS
# =====================================================


st.header(
    "Objectifs du projet"
)



st.markdown(
"""
Cette application permet de :

- Collecter automatiquement des données web avec Selenium
- Nettoyer et préparer les données avec Pandas
- Stocker les données dans une base SQL SQLite
- Explorer les résultats avec des dashboards interactifs
- Exporter les données collectées
- Evaluer l'expérience utilisateur via des formulaires dédiés
"""
)



st.divider()



# =====================================================
# PIPELINE DATA
# =====================================================


st.header(
    "Pipeline de traitement des données"
)



col1, col2, col3, col4 = st.columns(4)



with col1:

    st.subheader(
        "Collecte"
    )


    st.write(
"""
Selenium WebDriver

Sources :

- Books To Scrape
- Gaaraas Cars
"""
    )



with col2:

    st.subheader(
        "Nettoyage"
    )


    st.write(
"""
Pandas

Traitement :

- valeurs manquantes
- formats
- doublons
- transformation
"""
    )



with col3:

    st.subheader(
        "Stockage"
    )


    st.write(
"""
SQLite + SQLAlchemy

Tables :

- books
- cars
"""
    )



with col4:

    st.subheader(
        "Analyse"
    )


    st.write(
"""
Streamlit

Fonctionnalités :

- dashboards
- filtres
- export
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

    st.markdown(
"""
### Books To Scrape

Données collectées :

- Titre
- Prix
- Disponibilité
- Note
- Nombre de reviews
- Description
- Catégorie
- Taxe
"""
    )



with col2:

    st.markdown(
"""
### Gaaraas Cars

Données collectées :

- Marque
- Modèle
- Année
- Prix
- Kilométrage
- Transmission
- Région
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
Git/GitHub
"""
)



st.divider()



# =====================================================
# AUTEUR
# =====================================================


st.caption(
"""
Projet réalisé par Alpha Abdoulaye Lansar
Master Intelligence Artificielle

Data Collection Project
Web Scraping | Data Cleaning | Data Visualization | Deployment
"""
)