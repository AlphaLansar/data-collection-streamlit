import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os


st.set_page_config(
    page_title="Books Analytics Dashboard",
    layout="wide"
)



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



required_columns = [
    "title",
    "price",
    "rating",
    "product_type",
    "availability"
]


missing = [
    c for c in required_columns
    if c not in df.columns
]


if missing:

    st.error(
        f"Colonnes manquantes : {missing}"
    )

    st.write(
        df.columns.tolist()
    )

    st.stop()



st.title(
    "Books Analytics Dashboard"
)



st.write(
"""
Analyse du catalogue Books To Scrape.

Pipeline :
Selenium → Nettoyage Pandas → Dashboard Streamlit
"""
)



st.success(
    f"Dataset chargé : {len(df)} livres"
)



st.divider()



col1,col2,col3,col4 = st.columns(4)



col1.metric(
    "Nombre livres",
    len(df)
)



col2.metric(
    "Prix moyen",
    f"{df['price'].mean():.2f} £"
)



col3.metric(
    "Note moyenne",
    f"{df['rating'].mean():.2f}"
)



col4.metric(
    "Catégories",
    df["product_type"].nunique()
)



st.divider()



st.header(
    "Distribution prix"
)



fig,ax = plt.subplots()


ax.hist(
    df["price"],
    bins=15
)


st.pyplot(fig)



st.header(
    "Distribution notes"
)


st.bar_chart(
    df["rating"].value_counts()
)



st.header(
    "Catégories"
)


st.bar_chart(
    df["product_type"].value_counts()
)



st.dataframe(
    df,
    use_container_width=True
)