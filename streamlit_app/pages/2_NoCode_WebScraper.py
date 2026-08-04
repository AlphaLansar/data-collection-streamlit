import os
import pandas as pd
import streamlit as st


st.set_page_config(
    page_title="No-Code Web Scraper",
    page_icon="🕸️",
    layout="wide"
)



st.title(
    "No-Code Web Scraper"
)


st.markdown(
"""
Cette section présente la collecte des données réalisée avec
l'extension Chrome **Web Scraper**.

Contrairement au scraping Selenium présenté dans le pipeline
principal, cette partie correspond à une collecte **sans code**
et conserve les données dans leur état brut.

Pipeline :

Web Scraper Extension
↓
CSV brut
↓
Cleaning Pandas
↓
Analyse Dashboard
"""
)



st.divider()



BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )
)



# Chemins des fichiers no-code

FILES = {

    "Books - Web Scraper Raw":

        os.path.join(
            BASE_DIR,
            "data",
            "nocode",
            "books",
            "books.csv"
        ),


    "Cars - Web Scraper Raw":

        os.path.join(
            BASE_DIR,
            "data",
            "nocode",
            "cars",
            "cars.csv"
        )

}



st.header(
    "Datasets collectés avec Web Scraper"
)



for name, path in FILES.items():


    st.subheader(name)



    if not os.path.exists(path):

        st.warning(
            f"Fichier absent : {path}"
        )

        continue



    df = pd.read_csv(
        path
    )



    col1,col2,col3 = st.columns(3)



    with col1:

        st.metric(
            "Nombre de lignes",
            len(df)
        )


    with col2:

        st.metric(
            "Nombre de colonnes",
            len(df.columns)
        )


    with col3:

        st.metric(
            "Valeurs manquantes",
            int(
                df.isna()
                .sum()
                .sum()
            )
        )



    st.write(
        "Colonnes extraites :"
    )


    st.code(
        "\n".join(df.columns.tolist())
    )



    st.write(
        "Aperçu des données brutes :"
    )



    st.dataframe(
        df.head(20),
        use_container_width=True
    )



    csv = df.to_csv(
        index=False
    )



    st.download_button(

        label=f"Télécharger {os.path.basename(path)}",

        data=csv,

        file_name=os.path.basename(path),

        mime="text/csv"

    )


    st.divider()



st.header(
    "Méthodologie Web Scraper"
)



st.markdown(
"""
### Outil utilisé

Web Scraper Chrome Extension


### Procédure réalisée

1. Création d'un Sitemap.
2. Définition des sélecteurs HTML.
3. Configuration de la pagination.
4. Extraction des éléments.
5. Export CSV brut.


### Respect du cahier des charges

Cette partie respecte la contrainte :

✓ Scraping sans nettoyage  
✓ Utilisation d'un outil No-Code  
✓ Export des données brutes CSV  
✓ Séparation avec le scraping Selenium
"""
)



st.success(
"""
Module No-Code validé :

Web Scraper Extension
+
Raw CSV Export
+
Exploration Streamlit
"""
)