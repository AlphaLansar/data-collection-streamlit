import streamlit as st
import subprocess
import pandas as pd
import os


st.set_page_config(
    page_title="Scraping",
    layout="wide"
)


st.title("🕷️ Module Web Scraping")


st.write(
"""
Cette interface permet de lancer la collecte automatique
des données depuis les différentes sources.
"""
)



st.divider()



source = st.selectbox(
    "Choisir la source",
    [
        "Books To Scrape",
        "Gaaraas Cars"
    ]
)



pages = st.number_input(
    "Nombre de pages",
    min_value=1,
    max_value=100,
    value=5
)



st.divider()



if st.button(
    "🚀 Lancer scraping",
    type="primary"
):

    with st.spinner(
        "Scraping en cours..."
    ):


        if source == "Books To Scrape":


            scraper = [
                "python",
                "scraper/books_scraper.py",
                "--pages",
                str(pages)
            ]

            raw_file = "data/raw/books.csv"

            clean = [
                "python",
                "cleaning/clean_books.py"
            ]



        else:


            scraper = [
                "python",
                "scraper/cars_scraper.py",
                "--pages",
                str(pages)
            ]


            raw_file = "data/raw/cars.csv"


            clean = [
                "python",
                "cleaning/clean_cars.py"
            ]



        result = subprocess.run(
            scraper,
            capture_output=True,
            text=True
        )



        if result.returncode != 0:

            st.error(
                "Erreur scraping"
            )

            st.code(
                result.stderr
            )

            st.stop()



        st.success(
            "Scraping terminé"
        )


        st.code(
            result.stdout
        )



        # nettoyage automatique


        clean_result = subprocess.run(
            clean,
            capture_output=True,
            text=True
        )



        if clean_result.returncode == 0:

            st.success(
                "Nettoyage terminé"
            )


        else:

            st.warning(
                "Nettoyage échoué"
            )



st.divider()



st.header(
    "📊 Données brutes"
)



if source == "Books To Scrape":

    file = "data/raw/books.csv"

else:

    file = "data/raw/cars.csv"



if os.path.exists(file):


    df = pd.read_csv(file)



    col1,col2 = st.columns(2)



    with col1:

        st.metric(
            "Nombre lignes",
            len(df)
        )


    with col2:

        st.metric(
            "Nombre colonnes",
            len(df.columns)
        )



    st.dataframe(
        df.head(20),
        use_container_width=True
    )



else:


    st.info(
        "Aucune donnée disponible"
    )