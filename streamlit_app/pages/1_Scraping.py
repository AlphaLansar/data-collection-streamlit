import streamlit as st
import subprocess
import pandas as pd
import os


st.set_page_config(
    page_title="Scraping",
    layout="wide"
)



st.title("🕷️ Collecte des données - Web Scraping")


st.write(
"""
Cette interface permet de lancer les scripts Selenium
de collecte des données depuis les sources étudiées.
"""
)



st.divider()



# ============================
# CHOIX SOURCE
# ============================


source = st.selectbox(

    "Choisir la source à scraper",

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



if st.button("🚀 Lancer le scraping"):


    with st.spinner("Scraping en cours..."):


        try:


            if source == "Books To Scrape":


                command = [

                    "python",

                    "scraper/books_scraper.py",

                    "--pages",

                    str(pages)

                ]


                output_file = "data/raw/books.csv"



            else:


                command = [

                    "python",

                    "scraper/cars_scraper.py",

                    "--pages",

                    str(pages)

                ]


                output_file = "data/raw/cars.csv"




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


            else:


                st.error(
                    "Erreur pendant le scraping"
                )


                st.code(
                    result.stderr
                )



        except Exception as e:


            st.error(
                e
            )




st.divider()



# ============================
# APERCU RESULTATS
# ============================


st.header("📊 Aperçu des données collectées")



if source == "Books To Scrape":


    file="data/raw/books.csv"


else:


    file="data/raw/cars.csv"





if os.path.exists(file):


    df=pd.read_csv(file)



    st.metric(

        "Nombre de lignes",

        len(df)

    )



    st.dataframe(

        df.head(20),

        use_container_width=True

    )


else:


    st.info(
        "Aucune donnée disponible. Lancez un scraping."
    )