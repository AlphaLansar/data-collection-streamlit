import streamlit as st


st.set_page_config(
    page_title="Data Collection Platform",
    page_icon="📊",
    layout="wide"
)



st.title(
    "Data Collection & Analytics Platform"
)


st.write(
"""
Application développée dans le cadre du projet d'examen
Data Collection.

Cette plateforme permet de collecter, nettoyer, stocker
et analyser des données issues du Web scraping.
"""
)



st.divider()



st.header("Architecture du projet")



col1, col2, col3, col4 = st.columns(4)



with col1:

    st.subheader("1. Collecte")

    st.write(
    """
    Extraction automatique des données
    avec Selenium.

    Sources :

    - Books To Scrape
    - Gaaraas Cars
    """
    )



with col2:

    st.subheader("2. Préparation")

    st.write(
    """
    Nettoyage et transformation
    des données avec Pandas.
    """
    )



with col3:

    st.subheader("3. Stockage")

    st.write(
    """
    Base SQLite utilisant
    SQLAlchemy.

    Tables :

    - books
    - cars
    """
    )



with col4:

    st.subheader("4. Analyse")

    st.write(
    """
    Dashboards interactifs,
    statistiques et visualisations.
    """
    )



st.divider()



st.header("Sources de données")



col1, col2 = st.columns(2)



with col1:

    st.info(
    """
    Books To Scrape

    Variables principales :

    - titre
    - prix
    - disponibilité
    - note
    - reviews
    - catégorie
    - description
    - taxe
    """
    )



with col2:

    st.info(
    """
    Gaaraas Cars

    Variables principales :

    - marque
    - modèle
    - année
    - prix
    - kilométrage
    - transmission
    - région
    """
    )



st.divider()



st.header("Technologies")



st.write(
"""
Python | Selenium | Pandas | SQLAlchemy |
SQLite | Streamlit | Matplotlib
"""
)



st.divider()



st.caption(
"""
Projet réalisé par Alpha Abdoulaye Lansar
Master Intelligence Artificielle
Data Collection Project - 2026
"""
)