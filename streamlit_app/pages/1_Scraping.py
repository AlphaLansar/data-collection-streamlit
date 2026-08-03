import streamlit as st
import pandas as pd
import os


st.set_page_config(
    page_title="Scraping Pipeline",
    layout="wide"
)



st.title(
    "Web Scraping Pipeline"
)



st.markdown(
"""
## Phase 1 — Collecte des données

Cette interface présente la première étape du projet :

**Web Scraping automatique avec Selenium WebDriver**

Sources utilisées :

- Books To Scrape
- Gaaraas Dakar Cars

Technologies :

- Python
- Selenium
- Pandas
"""
)



st.divider()



# =====================================================
# PATH
# =====================================================


BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )
)



files = {


"Books Raw Dataset":
"data/raw/books.csv",


"Cars Raw Dataset":
"data/raw/cars.csv",


"Books Clean Dataset":
"data/cleaned/books_clean.csv",


"Cars Clean Dataset":
"data/cleaned/cars_clean.csv"

}



# =====================================================
# DATASET STATUS
# =====================================================


st.header(
"Etat des datasets"
)



cols = st.columns(4)



datasets = {}



for col,(name,path) in zip(cols,files.items()):


    file_path = os.path.join(
        BASE_DIR,
        path
    )


    with col:


        if os.path.exists(file_path):


            df = pd.read_csv(
                file_path
            )


            datasets[name] = df


            st.success(
                "Disponible"
            )


            st.metric(
                "Nombre lignes",
                len(df)
            )


            st.caption(
                f"{df.shape[1]} colonnes"
            )


        else:

            st.error(
                "Absent"
            )



st.divider()



# =====================================================
# DETAILS DATASET
# =====================================================


st.header(
"Détails des données collectées"
)



dataset_choice = st.selectbox(
    "Choisir un dataset",
    list(datasets.keys())
)



selected = datasets[dataset_choice]



col1,col2,col3 = st.columns(3)



with col1:

    st.metric(
        "Lignes",
        selected.shape[0]
    )



with col2:

    st.metric(
        "Colonnes",
        selected.shape[1]
    )



with col3:

    st.metric(
        "Valeurs manquantes",
        selected.isnull().sum().sum()
    )



st.subheader(
"Aperçu"
)


st.dataframe(
    selected.head(10),
    use_container_width=True
)



st.subheader(
"Colonnes disponibles"
)


st.write(
selected.columns.tolist()
)



st.divider()



# =====================================================
# ARCHITECTURE
# =====================================================


st.header(
"Architecture du pipeline"
)



st.code(
"""
                Selenium WebDriver

                       |
                       v

              Raw CSV Dataset

                       |
                       v

              Data Cleaning Pandas

                       |
                       v

             Clean CSV Dataset

                       |
                       v

              SQLite Database

                       |
                       v

          Streamlit Analytics Dashboard
"""
)



st.divider()



st.success(
"""
Pipeline Data Collection opérationnel :

Scraping
→ Cleaning
→ Database
→ Analytics
→ Visualization
"""
)