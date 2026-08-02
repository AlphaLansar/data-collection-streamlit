import streamlit as st

st.set_page_config(
    page_title="Application Evaluation",
    layout="wide"
)

# =====================================================
# MODIFIER CES DEUX LIENS
# =====================================================

GOOGLE_FORM_URL = "https://forms.gle/TON_LIEN_ICI"

KOBO_FORM_URL = "https://ee.kobotoolbox.org/x/TON_LIEN_ICI"

# =====================================================
# HEADER
# =====================================================

st.title("Application Evaluation")

st.write(
"""
Votre retour est important pour évaluer la qualité de cette application.

Deux versions du questionnaire sont disponibles conformément
aux exigences du projet :

• Google Forms

• KoboToolbox
"""
)

st.divider()

# =====================================================
# OBJECTIF
# =====================================================

st.header("Objectif de l'évaluation")

st.write(
"""
Le questionnaire permet d'évaluer :

- la qualité de l'interface

- la facilité d'utilisation

- les fonctionnalités proposées

- les performances générales

- la satisfaction globale

- les pistes d'amélioration
"""
)

st.divider()

# =====================================================
# FORMULAIRES
# =====================================================

col1, col2 = st.columns(2)

with col1:

    st.subheader("Google Forms")

    st.write(
"""
Version destinée aux utilisateurs souhaitant répondre
au questionnaire via Google Forms.
"""
    )

    st.link_button(
        "Accéder au formulaire Google Forms",
        GOOGLE_FORM_URL,
        use_container_width=True
    )

with col2:

    st.subheader("KoboToolbox")

    st.write(
"""
Version reproduisant le formulaire avec les logiques
conditionnelles demandées dans le sujet.
"""
    )

    st.link_button(
        "Accéder au formulaire KoboToolbox",
        KOBO_FORM_URL,
        use_container_width=True
    )

st.divider()

# =====================================================
# RAPPEL
# =====================================================

st.header("Informations")

st.info(
"""
Les deux formulaires contiennent les mêmes questions.

Ils permettent de recueillir les retours des utilisateurs
afin d'améliorer la plateforme.
"""
)

st.divider()

st.caption(
"""
Projet Data Collection

Développé par Alpha Abdoulaye Lansar

Master Intelligence Artificielle
"""
)