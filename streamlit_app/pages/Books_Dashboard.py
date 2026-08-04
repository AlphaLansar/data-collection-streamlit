import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os


st.set_page_config(
    page_title="Books Analytics",
    layout="wide"
)


# ==========================
# TITRE
# ==========================

st.title("Books Analytics Dashboard")


st.markdown(
"""
Analyse interactive du catalogue Books To Scrape.

Pipeline :
Web Scraping Selenium → Nettoyage Pandas → Analyse → Visualisation
"""
)


st.divider()



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



if df.empty:

    st.error(
        "Dataset vide"
    )

    st.stop()



st.success(
    f"{len(df)} livres chargés depuis le dataset nettoyé"
)



st.divider()



# ==========================
# KPI
# ==========================

st.header(
    "Indicateurs principaux"
)



c1,c2,c3,c4 = st.columns(4)



with c1:

    st.metric(
        "Nombre de livres",
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
        f"{df['rating'].mean():.2f}/5"
    )



with c4:

    st.metric(
        "Catégories",
        df["product_type"].nunique()
    )



st.divider()



# ==========================
# FILTRES
# ==========================

st.header(
    "Filtres interactifs"
)



col1,col2 = st.columns(2)



with col1:

    ratings = st.multiselect(
        "Sélectionner les notes",
        sorted(df["rating"].unique()),
        default=list(df["rating"].unique())
    )



with col2:

    availability = st.multiselect(
        "Disponibilité",
        sorted(df["availability"].unique()),
        default=list(df["availability"].unique())
    )



filtered = df[
    (df["rating"].isin(ratings))
    &
    (df["availability"].isin(availability))
]



st.write(
    f"Résultat : {len(filtered)} livres"
)



st.divider()



# ==========================
# TABLEAU
# ==========================


st.header(
    "Données filtrées"
)


st.dataframe(
    filtered,
    use_container_width=True
)



st.divider()



# ==========================
# GRAPHIQUES
# ==========================


st.header(
    "Analyses graphiques"
)



col1,col2 = st.columns(2)



# Prix

with col1:


    st.subheader(
        "Distribution des prix"
    )


    fig,ax = plt.subplots()


    ax.hist(
        filtered["price"],
        bins=20
    )


    ax.set_xlabel(
        "Prix (£)"
    )


    ax.set_ylabel(
        "Nombre de livres"
    )


    st.pyplot(fig)




# Rating

with col2:


    st.subheader(
        "Répartition des notes"
    )


    rating_count = (
        filtered["rating"]
        .value_counts()
        .sort_index()
    )


    fig,ax = plt.subplots()


    ax.bar(
        rating_count.index.astype(str),
        rating_count.values
    )


    ax.set_xlabel(
        "Note"
    )


    ax.set_ylabel(
        "Nombre"
    )


    st.pyplot(fig)




st.divider()



# ==========================
# TOP PRODUITS
# ==========================


st.header(
    "Livres les plus chers"
)



top_books = (
    filtered
    .sort_values(
        "price",
        ascending=False
    )
    [["title","price"]]
    .head(10)
)



st.dataframe(
    top_books,
    use_container_width=True
)