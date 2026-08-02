import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


st.set_page_config(
    page_title="Cars Dashboard",
    layout="wide"
)


st.title("🚗 Cars Data Dashboard")


FILE = "data/cleaned/cars_clean.csv"



@st.cache_data
def load_data():

    return pd.read_csv(FILE)



df = load_data()



st.sidebar.header("Filtres")



if "brand" in df.columns:

    brands = st.sidebar.multiselect(
        "Marque",
        df["brand"].dropna().unique(),
        default=df["brand"].dropna().unique()
    )

    df = df[df["brand"].isin(brands)]



if "year" in df.columns:

    years = st.sidebar.slider(
        "Année",
        int(df["year"].min()),
        int(df["year"].max()),
        (
            int(df["year"].min()),
            int(df["year"].max())
        )
    )

    df = df[
        (df["year"]>=years[0])
        &
        (df["year"]<=years[1])
    ]




st.subheader("📊 Informations générales")


col1,col2,col3,col4 = st.columns(4)



col1.metric(
    "Nombre voitures",
    len(df)
)


if "price" in df.columns:

    col2.metric(
        "Prix moyen",
        round(df["price"].mean(),0)
    )


if "year" in df.columns:

    col3.metric(
        "Année moyenne",
        round(df["year"].mean(),0)
    )


if "brand" in df.columns:

    col4.metric(
        "Marques",
        df["brand"].nunique()
    )



st.divider()



# Prix

if "price" in df.columns:

    st.subheader("💰 Distribution des prix")


    fig,ax = plt.subplots()


    ax.hist(
        df["price"].dropna(),
        bins=20
    )


    ax.set_xlabel(
        "Prix"
    )

    ax.set_ylabel(
        "Nombre voitures"
    )


    st.pyplot(fig)




# Marques

if "brand" in df.columns:


    st.subheader("🏷️ Marques populaires")


    brands_count = (
        df["brand"]
        .value_counts()
        .head(10)
    )


    st.bar_chart(
        brands_count
    )




# Année prix

if "year" in df.columns and "price" in df.columns:


    st.subheader(
        "📈 Relation année / prix"
    )


    fig,ax = plt.subplots()


    ax.scatter(
        df["year"],
        df["price"]
    )


    ax.set_xlabel(
        "Année"
    )


    ax.set_ylabel(
        "Prix"
    )


    st.pyplot(fig)




# Tableau

st.subheader(
    "📋 Données voitures"
)


st.dataframe(
    df,
    use_container_width=True
)



st.success(
    "Dashboard Cars opérationnel"
)