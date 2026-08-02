import streamlit as st
import pandas as pd
import os


st.set_page_config(
    page_title="Download Data",
    layout="wide"
)


st.title("⬇️ Téléchargement des données")


st.write(
"""
Cette page permet de télécharger les données collectées
par scraping ainsi que les données nettoyées utilisées
dans les dashboards.
"""
)



st.divider()



# ============================
# BOOKS
# ============================


st.header("📚 Books To Scrape")


books_files = {

    "Données brutes Books (Selenium)":
    "data/raw/books.csv",

    "Données nettoyées Books":
    "data/cleaned/books_clean.csv"

}



for name,path in books_files.items():


    if os.path.exists(path):

        with open(
            path,
            "rb"
        ) as file:


            st.download_button(

                label=f"⬇️ {name}",

                data=file,

                file_name=os.path.basename(path),

                mime="text/csv"

            )

    else:

        st.warning(
            f"{path} introuvable"
        )



st.divider()



# ============================
# CARS
# ============================


st.header("🚗 Gaaraas Cars")



cars_files = {


    "Données brutes Cars (Selenium)":
    "data/raw/cars.csv",


    "Données nettoyées Cars":
    "data/cleaned/cars_clean.csv"

}



for name,path in cars_files.items():


    if os.path.exists(path):

        with open(
            path,
            "rb"
        ) as file:


            st.download_button(

                label=f"⬇️ {name}",

                data=file,

                file_name=os.path.basename(path),

                mime="text/csv"

            )


    else:

        st.warning(
            f"{path} introuvable"
        )



st.divider()



# ============================
# DATABASE
# ============================


st.header("🗄️ Base de données SQL")



database="books_cars.db"



if os.path.exists(database):


    with open(
        database,
        "rb"
    ) as file:


        st.download_button(

            label="⬇️ Télécharger la base SQLite",

            data=file,

            file_name="books_cars.db",

            mime="application/octet-stream"

        )


else:

    st.warning(
        "Base SQLite non trouvée"
    )



st.success(
"Module téléchargement opérationnel"
)