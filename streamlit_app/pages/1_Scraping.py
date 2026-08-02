import streamlit as st
import subprocess
import pandas as pd
import os
import time



st.set_page_config(
    page_title="Selenium Scraping",
    layout="wide"
)



st.title(
    "Selenium Web Scraping"
)



st.write(
"""
Module de collecte automatique des données
depuis les sources web du projet.

Technologie utilisée :
- Selenium WebDriver
- Python
- Pandas
"""
)



st.divider()



# ===============================
# PARAMETRES SCRAPING
# ===============================


st.header(
    "Configuration du scraping"
)



col1, col2 = st.columns(2)



with col1:

    source = st.selectbox(
        "Source de données",
        [
            "Books To Scrape",
            "Gaaraas Cars"
        ]
    )



with col2:

    pages = st.number_input(
        "Nombre de pages à scraper",
        min_value=1,
        max_value=100,
        value=5
    )



st.divider()



# ===============================
# LANCEMENT
# ===============================


if st.button(
    "Lancer le scraping"
):


    progress = st.progress(0)


    status = st.empty()



    try:


        if source == "Books To Scrape":


            command = [
                "python",
                "scraper/books_scraper.py",
                "--pages",
                str(pages)
            ]


            output_file = (
                "data/raw/books.csv"
            )


        else:


            command = [
                "python",
                "scraper/cars_scraper.py",
                "--pages",
                str(pages)
            ]


            output_file = (
                "data/raw/cars.csv"
            )



        status.info(
            "Scraping en cours..."
        )


        progress.progress(30)



        result = subprocess.run(
            command,
            capture_output=True,
            text=True
        )



        progress.progress(80)



        if result.returncode == 0:


            progress.progress(100)


            st.success(
                "Scraping terminé avec succès"
            )



            st.subheader(
                "Logs Selenium"
            )


            st.code(
                result.stdout
            )



            if os.path.exists(output_file):


                df = pd.read_csv(
                    output_file
                )


                st.metric(
                    "Nombre de lignes collectées",
                    len(df)
                )


                with st.expander(
                    "Aperçu des données"
                ):

                    st.dataframe(
                        df.head(10),
                        use_container_width=True
                    )



        else:


            st.error(
                "Erreur pendant le scraping"
            )


            st.code(
                result.stderr
            )



    except Exception as e:


        st.error(
            str(e)
        )



st.divider()



# ===============================
# INFORMATION
# ===============================


st.header(
    "Sources disponibles"
)



col1,col2 = st.columns(2)



with col1:


    st.info(
"""
Books To Scrape

Pagination :
Toutes les pages du catalogue

Variables :
- titre
- prix
- disponibilité
- rating
- reviews
- description
- catégorie
- tax
"""
    )



with col2:


    st.info(
"""
Gaaraas Cars

Pagination :
Pages des annonces Dakar Auto

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



st.caption(
"""
Data Collection Project - Selenium Scraping Module
"""
)