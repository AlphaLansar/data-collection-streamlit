import streamlit as st


st.set_page_config(
    page_title="Evaluation Application",
    layout="centered"
)


st.title("📝 Évaluation de l'application")


st.write(
"""
Votre avis nous aide à améliorer cette application de collecte,
nettoyage et visualisation des données.
"""
)



st.divider()



# =========================
# Google Form
# =========================

st.subheader(
    "📄 Formulaire Google Forms"
)


google_form_url = (
    "https://docs.google.com/forms/"
)


st.markdown(
f"""
<a href="{google_form_url}" target="_blank">
<button style="
background-color:#4285F4;
color:white;
padding:10px 20px;
border:none;
border-radius:5px;
">
Ouvrir Google Forms
</button>
</a>
""",
unsafe_allow_html=True
)



st.divider()



# =========================
# Kobo Form
# =========================


st.subheader(
    "📱 Formulaire Kobo"
)


kobo_url = (
    "https://kf.kobotoolbox.org/"
)



st.markdown(
f"""
<a href="{kobo_url}" target="_blank">
<button style="
background-color:#28a745;
color:white;
padding:10px 20px;
border:none;
border-radius:5px;
">
Ouvrir Kobo Form
</button>
</a>
""",
unsafe_allow_html=True
)



st.divider()



st.info(
"""
Merci pour votre précieux retour !

Vos commentaires nous aideront à améliorer l’application.
"""
)