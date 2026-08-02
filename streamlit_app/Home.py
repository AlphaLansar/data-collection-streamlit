import streamlit as st


st.set_page_config(
    page_title="Data Collection Dashboard",
    page_icon="📊",
    layout="wide"
)



st.title(
    "📊 Data Collection Dashboard"
)



st.markdown(
"""
Bienvenue dans l'application de visualisation des données collectées.

Sources disponibles :

- 📚 Books Dataset
- 🚗 Cars Dataset

Fonctionnalités :

✅ Visualisation des données  
✅ Recherche et filtres  
✅ Statistiques  
✅ Export CSV  
"""
)



st.info(
    "Utilisez le menu à gauche pour accéder aux différents dashboards."
)