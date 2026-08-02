import streamlit as st


st.set_page_config(
    page_title="Data Collection Application",
    page_icon="📊",
    layout="wide"
)



st.title(
    "📊 Data Collection & Analysis Platform"
)



st.write(
"""
Bienvenue dans notre application de collecte,
nettoyage et analyse de données.

Cette plateforme permet :

- 🕷️ Collecter automatiquement les données web
- 🧹 Nettoyer les données collectées
- 📥 Télécharger les données brutes
- 📊 Visualiser les résultats avec des dashboards interactifs
- 📝 Evaluer l'application
"""
)



st.divider()



st.header(
    "🚀 Modules disponibles"
)



col1,col2,col3,col4 = st.columns(4)



with col1:

    st.subheader(
        "🕷️ Scraping"
    )

    st.write(
    """
    Collecte automatique des données
    depuis les sources web.
    
    Sources :
    - Books To Scrape
    - Gaaraas Cars
    """
    )



with col2:

    st.subheader(
        "⬇️ Download"
    )

    st.write(
    """
    Téléchargement des données
    brutes issues du scraping.
    """
    )



with col3:

    st.subheader(
        "📊 Dashboard"
    )

    st.write(
    """
    Exploration interactive :
    
    - statistiques
    - graphiques
    - filtres
    """
    )



with col4:

    st.subheader(
        "📝 Evaluation"
    )

    st.write(
    """
    Donner votre avis
    sur l'application.
    """
    )



st.divider()



st.header(
    "📌 Sources de données"
)



col1,col2 = st.columns(2)



with col1:

    st.success(
    """
    📚 Books To Scrape

    Variables :
    - titre
    - prix
    - disponibilité
    - rating
    - catégorie
    - reviews
    - description
    """
    )



with col2:

    st.info(
    """
    🚗 Gaaraas Cars

    Variables :
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



st.header(
    "🛠️ Technologies utilisées"
)



st.write(
"""
Python | Selenium | BeautifulSoup | Pandas | SQL SQLite | Streamlit | Matplotlib
"""
)



st.divider()



st.caption(
"""
Projet d'examen Data Collection - Web Scraping, Cleaning and Deployment
"""
)