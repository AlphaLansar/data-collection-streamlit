import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os


st.set_page_config(
    page_title="Books Analytics Dashboard",
    layout="wide"
)


st.title(
    "Books Analytics Dashboard"
)


st.write(
"""
Analyse interactive des livres collectés
depuis Books to Scrape.

Pipeline :
Scraping Selenium → Cleaning Pandas → Analyse → Dashboard
"""
)



# ==========================
# DATASET
# ==========================

BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )
)


FILE = os.path.join(
    BASE_DIR,
    "data",
    "cleaned",
    "books_clean.csv"
)



@st.cache_data
def load_data():

    return pd.read_csv(FILE)



df = load_data()



st.success(
    f"Dataset chargé : {len(df)} livres"
)



# ==========================
# INDICATEURS
# ==========================


st.header(
    "Indicateurs principaux"
)



c1,c2,c3,c4 = st.columns(4)



with c1:

    st.metric(
        "Nombre livres",
        len(df)
    )



with c2:

    st.metric(
        "Prix moyen",
        f"{df['price'].mean():.2f} £"
    )



with c3:

    st.metric(
        "Note moyenne",
        round(
            df["rating"].mean(),
            2
        )
    )



with c4:

    st.metric(
        "Types de livres",
        df["product_type"].nunique()
    )



st.divider()



# ==========================
# TABLE
# ==========================

st.header(
    "Données livres"
)


st.dataframe(
    df,
    use_container_width=True
)



st.divider()



# ==========================
# GRAPHIQUES
# ==========================


st.header(
    "Visualisations"
)



col1,col2 = st.columns(2)



with col1:

    st.subheader(
        "Distribution des prix"
    )


    fig,ax = plt.subplots()


    ax.hist(
        df["price"],
        bins=20
    )


    ax.set_xlabel(
        "Prix (£)"
    )


    ax.set_ylabel(
        "Nombre de livres"
    )


    st.pyplot(fig)



with col2:


    st.subheader(
        "Répartition des notes"
    )


    rating_count = (
        df["rating"]
        .value_counts()
        .sort_index()
    )


    fig,ax = plt.subplots()


    ax.bar(
        rating_count.index,
        rating_count.values
    )


    ax.set_xlabel(
        "Note"
    )


    ax.set_ylabel(
        "Nombre"
    )


    st.pyplot(fig)