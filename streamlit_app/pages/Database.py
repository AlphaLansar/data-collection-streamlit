import streamlit as st
import sqlite3
import pandas as pd
import os


st.set_page_config(
    page_title="Database Explorer",
    layout="wide"
)


st.title("Database Explorer - SQLite")


st.markdown(
"""
Exploration interactive de la base de données intégrée au projet.

Pipeline :

Web Scraping  
↓  
Data Cleaning  
↓  
SQLite Database  
↓  
Analytics Dashboard
"""
)


st.divider()



# =====================================================
# CONNEXION DATABASE
# =====================================================


BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )
)


DB_PATH = os.path.join(
    BASE_DIR,
    "books_cars.db"
)



@st.cache_resource
def get_connection():

    return sqlite3.connect(
        DB_PATH,
        check_same_thread=False
    )



conn = get_connection()



# =====================================================
# VERIFICATION
# =====================================================


if not os.path.exists(DB_PATH):

    st.error(
        "Base SQLite introuvable"
    )

    st.stop()



st.success(
    "Connexion SQLite réussie"
)



st.divider()



# =====================================================
# INFORMATIONS GENERALES
# =====================================================


tables = pd.read_sql(
"""
SELECT name
FROM sqlite_master
WHERE type='table';
""",
conn
)



c1,c2,c3 = st.columns(3)



with c1:

    st.metric(
        "Nombre de tables",
        len(tables)
    )



with c2:

    st.metric(
        "SGBD",
        "SQLite"
    )



with c3:

    st.metric(
        "Base",
        "books_cars.db"
    )



st.subheader(
    "Tables disponibles"
)


st.dataframe(
    tables,
    use_container_width=True
)



st.divider()



# =====================================================
# EXPLORATION
# =====================================================


st.header(
    "Exploration SQL"
)



table_name = st.selectbox(
    "Choisir une table",
    tables["name"].tolist()
)



query_count = f"""
SELECT COUNT(*) as total
FROM {table_name}
"""


count = pd.read_sql(
    query_count,
    conn
)["total"][0]



columns = pd.read_sql(
f"""
PRAGMA table_info({table_name});
""",
conn
)



c1,c2,c3 = st.columns(3)



with c1:

    st.metric(
        "Nombre lignes",
        count
    )



with c2:

    st.metric(
        "Nombre colonnes",
        len(columns)
    )



with c3:

    missing = pd.read_sql(
f"""
SELECT *
FROM {table_name}
""",
conn
).isnull().sum().sum()


    st.metric(
        "Valeurs manquantes",
        missing
    )



st.divider()



# =====================================================
# APERCU
# =====================================================


st.header(
    "Aperçu des données"
)


limit = st.slider(
    "Nombre de lignes",
    5,
    100,
    10
)



data = pd.read_sql(
f"""
SELECT *
FROM {table_name}
LIMIT {limit}
""",
conn
)



st.dataframe(
    data,
    use_container_width=True
)



st.divider()



# =====================================================
# STRUCTURE
# =====================================================


st.header(
    "Structure de la table"
)



structure = columns[
[
"name",
"type",
"notnull"
]
]


structure.columns = [
"Colonne",
"Type",
"Obligatoire"
]



st.dataframe(
structure,
use_container_width=True
)



st.divider()



# =====================================================
# STATISTIQUES
# =====================================================


st.header(
    "Statistiques numériques"
)


numeric = data.select_dtypes(
include=["number"]
)



if len(numeric.columns)>0:

    st.dataframe(
        numeric.describe(),
        use_container_width=True
    )


else:

    st.info(
        "Aucune colonne numérique disponible"
    )



st.divider()



# =====================================================
# VALIDATION PROJET
# =====================================================


st.success(
"""
Cette interface valide la partie :

Database Integration

du projet Data Collection :

Scraping → Cleaning → SQLite → Dashboard
"""
)