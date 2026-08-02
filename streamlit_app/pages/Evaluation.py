import streamlit as st


st.set_page_config(
    page_title="Evaluation Application",
    page_icon="📝",
    layout="wide"
)


# ==========================
# HEADER
# ==========================

st.title("📝 Évaluation de l'application")

st.markdown(
"""
Cette section permet aux utilisateurs d'évaluer l'application
de collecte, nettoyage, stockage et visualisation des données.

Deux versions du formulaire sont disponibles :
- Google Forms
- KoboToolbox
"""
)


st.divider()



# ==========================
# FORMULAIRES
# ==========================


col1, col2 = st.columns(2)



with col1:

    st.subheader("📄 Google Forms")

    st.write(
    """
    Version Google du formulaire d'évaluation.

    Elle permet de collecter :
    - informations utilisateur
    - expérience utilisateur
    - satisfaction globale
    - suggestions d'amélioration
    """
    )


    google_url = "https://docs.google.com/forms/"


    st.link_button(
        "Ouvrir Google Forms",
        google_url
    )



with col2:

    st.subheader("📱 KoboToolBox")


    st.write(
    """
    Version mobile du formulaire.

    Adaptée pour :
    - collecte terrain
    - utilisation smartphone
    - enquêtes utilisateurs
    """
    )


    kobo_url = "https://kf.kobotoolbox.org/"


    st.link_button(
        "Ouvrir Kobo Form",
        kobo_url
    )



st.divider()



# ==========================
# STRUCTURE EVALUATION
# ==========================


st.header("📋 Structure du formulaire")


sections = {

"1️⃣ Informations utilisateur":
[
"Date de l'évaluation",
"Nom (optionnel)",
"Rôle / profession",
"Plateforme utilisée",
"Première utilisation"
],


"2️⃣ Interface utilisateur":
[
"Design de l'application",
"Navigation",
"Clarté des menus",
"Temps de chargement",
"Compatibilité appareil"
],


"3️⃣ Fonctionnalités":
[
"Scraping des données",
"Téléchargement",
"Formulaires",
"Dashboards"
],


"4️⃣ Problèmes rencontrés":
[
"Erreurs",
"Affichage",
"Performance",
"Fonctionnalités non disponibles"
],


"5️⃣ Satisfaction globale":
[
"Note sur 10",
"Niveau de satisfaction",
"Recommandation",
"Réutilisation"
],


"6️⃣ Suggestions":
[
"Points forts",
"Axes d'amélioration",
"Fonctionnalités souhaitées"
]

}



for title, questions in sections.items():

    with st.expander(title):

        for q in questions:

            st.write("✓", q)



st.divider()



# ==========================
# MESSAGE FINAL
# ==========================


st.success(
"""
Merci pour votre précieux retour !

Vos commentaires nous aideront à améliorer l’application.
"""
)