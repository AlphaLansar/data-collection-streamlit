import streamlit as st
import pandas as pd
import os


st.set_page_config(
    page_title="Download Data",
    page_icon="⬇️",
    layout="wide"
)


st.title("⬇️ Download Data")


st.write(
"""
Cette page permet de télécharger les données utilisées dans le projet.

Sources disponibles :

- Données brutes issues du scraping Selenium
- Données nettoyées utilisées pour les dashboards
- Données brutes issues du scraping no-code Web Scraper
"""
)


st.divider()



# =====================================================
# FONCTION TELECHARGEMENT
# =====================================================


def download_section(title, file_path):


    st.subheader(title)


    if os.path.exists(file_path):


        df = pd.read_csv(file_path)


        st.success(
            f"Données disponibles : {len(df)} lignes"
        )


        with st.expander("Voir aperçu"):

            st.dataframe(
                df.head(10),
                use_container_width=True
            )


        with open(
            file_path,
            "rb"
        ) as file:


            st.download_button(

                label="⬇️ Télécharger CSV",

                data=file,

                file_name=os.path.basename(file_path),

                mime="text/csv"

            )


    else:


        st.warning(
            "Fichier non disponible pour le moment"
        )



# =====================================================
# SELENIUM RAW DATA
# =====================================================


st.header(
    "🕷️ Données brutes Selenium"
)



download_section(

    "📚 Books Raw Selenium",

    "data/raw/books.csv"

)


download_section(

    "🚗 Cars Raw Selenium",

    "data/raw/cars.csv"

)



st.divider()



# =====================================================
# CLEAN DATA
# =====================================================


st.header(
    "🧹 Données nettoyées"
)



download_section(

    "📚 Books Clean Dataset",

    "data/cleaned/books_clean.csv"

)



download_section(

    "🚗 Cars Clean Dataset",

    "data/cleaned/cars_clean.csv"

)



st.divider()



# =====================================================
# WEB SCRAPER NO CODE
# =====================================================


st.header(
    "🌐 Web Scraper No-Code"
)



st.info(
"""
Les fichiers issus de l'extension Chrome Web Scraper
seront ajoutés ici.

Format attendu :

data/nocode/

    books_webscraper_raw.csv

    cars_webscraper_raw.csv
"""
)



download_section(

    "📚 Books Web Scraper Raw",

    "data/nocode/books_webscraper_raw.csv"

)



download_section(

    "🚗 Cars Web Scraper Raw",

    "data/nocode/cars_webscraper_raw.csv"

)



st.divider()



st.caption(
"""
Projet Data Collection - Web Scraping, Cleaning and Streamlit Deployment
"""
)