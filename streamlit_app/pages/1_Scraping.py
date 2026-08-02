import streamlit as st
import subprocess
import pandas as pd
import os



st.set_page_config(
    page_title="Web Scraping",
    layout="wide"
)



st.title(
    "Web Scraping Module"
)



st.write(
"""
Cette interface permet de lancer la collecte automatique
des données avec Selenium WebDriver.

Sources disponibles :

- Books To Scrape
- Gaaraas Cars
"""
)



st.divider()



# ===============================
# CONFIGURATION
# ===============================


st.header(
    "Configuration du scraping"
)



source = st.selectbox(

    "Choisir la source",

    [
        "Books To Scrape",
        "Gaaraas Cars"
    ]

)



pages = st.number_input(

    "Nombre de pages à scraper",

    min_value=1,

    max_value=100,

    value=5

)



st.divider()



# ===============================
# LANCEMENT SCRAPING
# ===============================


if st.button(
    "Lancer la collecte"
):


    with st.spinner(
        "Collecte Selenium en cours..."
    ):


        if source == "Books To Scrape":


            command = [

                "python",

                "scraper/books_scraper.py",

                "--pages",

                str(pages)

            ]


            output = (
                "data/raw/books.csv"
            )



        else:


            command = [

                "python",

                "scraper/cars_scraper.py",

                "--pages",

                str(pages)

            ]


            output = (
                "data/raw/cars.csv"
            )



        try:


            result = subprocess.run(

                command,

                capture_output=True,

                text=True

            )



            if result.returncode == 0:


                st.success(
                    "Scraping terminé avec succès"
                )


                st.code(
                    result.stdout
                )



                if os.path.exists(output):


                    df = pd.read_csv(output)


                    st.subheader(
                        "Résultat de la collecte"
                    )


                    col1,col2 = st.columns(2)


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
                f"Erreur système : {e}"
            )



st.divider()



# ===============================
# ETAT DES DONNEES
# ===============================


st.header(
    "Etat des données disponibles"
)



files = [

    (
        "Books Raw Selenium",
        "data/raw/books.csv"
    ),

    (
        "Cars Raw Selenium",
        "data/raw/cars.csv"
    )

]



for name,path in files:


    if os.path.exists(path):


        df = pd.read_csv(path)


        st.success(

            f"{name} : {df.shape[0]} lignes disponibles"

        )


    else:


        st.warning(

            f"{name} : fichier absent"

        )



st.caption(
"""
Collecte réalisée avec Selenium WebDriver
Projet Data Collection - Alpha Abdoulaye Lansar
"""
)