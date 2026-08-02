import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os


st.set_page_config(
    page_title="Books Dashboard",
    layout="wide"
)


st.title("📚 Books Data Dashboard")


FILE = "data/cleaned/books_clean.csv"


@st.cache_data
def load_data():

    return pd.read_csv(FILE)



df = load_data()



st.sidebar.header("Filtres")


ratings = st.sidebar.multiselect(
    "Note",
    options=df["rating"].unique(),
    default=df["rating"].unique()
)


categories = st.sidebar.multiselect(
    "Catégorie",
    options=df["product_type"].unique(),
    default=df["product_type"].unique()
)



filtered = df[
    (df["rating"].isin(ratings))
    &
    (df["product_type"].isin(categories))
]



st.subheader("📊 Informations générales")


col1,col2,col3,col4 = st.columns(4)


col1.metric(
    "Nombre livres",
    len(filtered)
)


col2.metric(
    "Prix moyen",
    round(filtered["price"].mean(),2)
)


col3.metric(
    "Prix maximum",
    round(filtered["price"].max(),2)
)


col4.metric(
    "Catégories",
    filtered["product_type"].nunique()
)



st.divider()



st.subheader("💰 Distribution des prix")


fig,ax = plt.subplots()

ax.hist(
    filtered["price"],
    bins=20
)

ax.set_xlabel("Prix")
ax.set_ylabel("Nombre")


st.pyplot(fig)



st.subheader("⭐ Distribution des notes")


rating_count = filtered["rating"].value_counts()


fig,ax = plt.subplots()

ax.bar(
    rating_count.index,
    rating_count.values
)

ax.set_xlabel("Note")
ax.set_ylabel("Nombre")


st.pyplot(fig)



st.subheader("📦 Disponibilité")


availability = filtered["availability"].value_counts()


st.bar_chart(
    availability
)



st.subheader("🏷️ Catégories")


category = filtered["product_type"].value_counts()


st.bar_chart(
    category
)



st.subheader("🔥 Livres les plus chers")


top = filtered.sort_values(
    "price",
    ascending=False
).head(10)


st.dataframe(
    top[
        [
            "title",
            "price",
            "rating",
            "product_type"
        ]
    ],
    use_container_width=True
)



st.success(
    "Dashboard Books opérationnel"
)