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
Cette section permet aux utilisateurs d'évaluer
l'expérience utilisateur de la plateforme.

Deux versions du formulaire sont disponibles :
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
    Version Google Forms du questionnaire
    d'évaluation utilisateur.
    """
    )


    google_url = st.text_input(
        "Lien Google Forms",
        value=""
    )


    if google_url:

        st.link_button(
            "Ouvrir Google Forms",
            google_url
        )




with col2:

    st.subheader(
        "KoboToolbox"
    )


    st.write(
    """
    Version KoboToolbox du questionnaire
    avec logique conditionnelle.
    """
    )


    kobo_url = st.text_input(
        "Lien Kobo",
        value=""
    )


    if kobo_url:

        st.link_button(
            "Ouvrir Kobo Form",
            kobo_url
        )



st.divider()



st.info(
"""
Les liens définitifs seront ajoutés après
la création des formulaires officiels.
"""
)



st.caption(
"""
Data Collection Project - Evaluation Module
"""
)