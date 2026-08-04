import streamlit as st


st.set_page_config(
    page_title="Application Evaluation",
    layout="wide"
)



st.title(
    "Application Evaluation"
)



st.write(
"""
Cette section permet d'évaluer l'expérience utilisateur
de la plateforme Data Collection.

Deux formulaires sont disponibles :
- Google Forms
- KoboToolbox
"""
)



st.divider()



st.header(
    "Formulaires d'évaluation"
)



col1, col2 = st.columns(2)



with col1:

    st.subheader(
        "Google Forms"
    )


    st.write(
    """
    Formulaire Google Forms pour recueillir
    les retours des utilisateurs.
    """
    )


    google_url = (
        "https://docs.google.com/forms/d/e/"
        "1FAIpQLSd8dvtFMb5g0aOYOZJt592TYf6_tej7HMSJuaTEC5BOAYA2Ug/"
        "viewform?usp=dialog"
    )


    st.link_button(
        "📝 Remplir Google Forms",
        google_url
    )



with col2:

    st.subheader(
        "KoboToolbox"
    )


    st.write(
    """
    Formulaire KoboToolbox utilisant XLSForm
    avec logique conditionnelle et validation.
    """
    )


    kobo_url = (
        "https://ee.kobotoolbox.org/x/O8ODJ0sY"
    )


    st.link_button(
        "📊 Remplir KoboToolbox",
        kobo_url
    )



st.divider()



st.success(
"""
Les deux formulaires d'évaluation sont disponibles.

Les données collectées permettront d'analyser :
- l'expérience utilisateur
- la satisfaction
- les problèmes rencontrés
- les suggestions d'amélioration
"""
)



st.caption(
"""
Data Collection Project
Web Scraping | Data Cleaning | Data Visualization | Evaluation

Réalisé par Alpha Abdoulaye Lansar
Master Intelligence Artificielle
"""
)