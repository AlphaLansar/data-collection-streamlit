import streamlit as st
import pandas as pd
import sqlite3
import os


st.set_page_config(
    page_title="Data Export Center",
    layout="wide"
)


st.title("Data Export Center")


st.markdown(
"""
Centre d'exportation des données du projet.

Pipeline :

Scraping
↓
Cleaning
↓
SQLite Database
↓
Export des données
"""
)


st.divider()



# =====================================================
# PATHS
# =====================================================


BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )
)



BOOKS_FILE = os.path.join(
    BASE_DIR,
    "data",
    "cleaned",
    "books_clean.csv"
)


CARS_FILE = os.path.join(
    BASE_DIR,
    "data",
    "cleaned",
    "cars_clean.csv"
)



DB_FILE = os.path.join(
    BASE_DIR,
    "books_cars.db"
)



# =====================================================
# LOAD DATA
# =====================================================


@st.cache_data
def load_books():

    return pd.read_csv(
        BOOKS_FILE
    )


@st.cache_data
def load_cars():

    return pd.read_csv(
        CARS_FILE
    )



books = load_books()

cars = load_cars()



# =====================================================
# STATISTICS
# =====================================================


st.header(
    "Données disponibles"
)



col1,col2,col3 = st.columns(3)



with col1:

    st.metric(
        "Livres nettoyés",
        len(books)
    )



with col2:

    st.metric(
        "Voitures nettoyées",
        len(cars)
    )



with col3:

    st.metric(
        "Base SQLite",
        "Disponible"
    )



st.divider()



# =====================================================
# CSV EXPORT
# =====================================================


st.header(
    "Export CSV"
)



col1,col2 = st.columns(2)



with col1:

    st.subheader(
        "Books Dataset"
    )


    csv_books = books.to_csv(
        index=False
    )


    st.download_button(
        label="Télécharger books_clean.csv",
        data=csv_books,
        file_name="books_clean.csv",
        mime="text/csv"
    )



with col2:

    st.subheader(
        "Cars Dataset"
    )


    csv_cars = cars.to_csv(
        index=False
    )


    st.download_button(
        label="Télécharger cars_clean.csv",
        data=csv_cars,
        file_name="cars_clean.csv",
        mime="text/csv"
    )



st.divider()



# =====================================================
# SQLITE EXPORT
# =====================================================


st.header(
    "Export Base de données SQLite"
)



if os.path.exists(DB_FILE):


    with open(
        DB_FILE,
        "rb"
    ) as file:


        st.download_button(
            label="Télécharger books_cars.db",
            data=file,
            file_name="books_cars.db",
            mime="application/octet-stream"
        )


    st.success(
        "Base SQLite prête pour export"
    )


else:

    st.error(
        "Base SQLite introuvable"
    )



st.divider()



# =====================================================
# DATABASE PREVIEW
# =====================================================


st.header(
    "Aperçu des tables SQL"
)



conn = sqlite3.connect(
    DB_FILE
)



tables = pd.read_sql(
"""
SELECT name
FROM sqlite_master
WHERE type='table';
""",
conn
)



st.dataframe(
    tables,
    use_container_width=True
)



table = st.selectbox(
    "Prévisualiser une table",
    tables["name"]
)



preview = pd.read_sql(
f"""
SELECT *
FROM {table}
LIMIT 10
""",
conn
)



st.dataframe(
preview,
use_container_width=True
)



conn.close()



st.success(
"""
Module Export validé :

CSV Cleaning Export
+
SQLite Database Export
"""
)