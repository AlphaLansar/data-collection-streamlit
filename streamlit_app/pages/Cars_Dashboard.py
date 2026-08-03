import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os


# =====================================================
# CONFIGURATION
# =====================================================

st.set_page_config(
    page_title="Cars Analytics Dashboard",
    page_icon="🚗",
    layout="wide"
)



# =====================================================
# CHEMIN PROJET
# =====================================================

PROJECT_DIR = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        "../.."
    )
)


DATA_FILE = os.path.join(
    PROJECT_DIR,
    "data",
    "cleaned",
    "cars_clean.csv"
)



# =====================================================
# HEADER
# =====================================================

st.title(
    "Cars Analytics Dashboard"
)


st.markdown(
"""
### Analyse interactive des annonces automobiles

Source :
**Gaaraas - Dakar Auto**

Pipeline :

**Selenium Scraping → Cleaning Pandas → Analyse → Visualisation**
"""
)



st.divider()



# =====================================================
# CHARGEMENT
# =====================================================


@st.cache_data
def load_cars():

    return pd.read_csv(DATA_FILE)



try:

    df = load_cars()


except Exception as e:

    st.error(
        "Erreur chargement dataset voitures"
    )

    st.write(e)

    st.stop()



# =====================================================
# VERIFICATION DATASET
# =====================================================


required_columns = [

    "title",
    "brand",
    "model",
    "year",
    "region",
    "price",
    "mileage",
    "transmission"

]


missing = [

    col for col in required_columns

    if col not in df.columns

]



if missing:

    st.error(
        "Le dashboard ne charge pas cars_clean.csv"
    )


    st.write(
        "Fichier chargé :"
    )


    st.code(
        DATA_FILE
    )


    st.write(
        "Colonnes trouvées :"
    )


    st.write(
        df.columns.tolist()
    )


    st.stop()



st.success(
    f"Dataset voitures chargé : {len(df)} annonces"
)



st.divider()



# =====================================================
# KPI
# =====================================================


st.header(
    "Indicateurs principaux"
)



c1,c2,c3,c4 = st.columns(4)



with c1:

    st.metric(
        "Nombre véhicules",
        len(df)
    )



with c2:

    st.metric(
        "Prix moyen",
        f"{df['price'].mean():,.0f} FCFA"
    )



with c3:

    st.metric(
        "Marques",
        df["brand"].nunique()
    )



with c4:

    st.metric(
        "Kilométrage moyen",
        f"{df['mileage'].mean():,.0f} km"
    )



st.divider()



# =====================================================
# FILTRES
# =====================================================


st.header(
    "Filtres"
)



col1,col2,col3 = st.columns(3)



with col1:

    brands = st.multiselect(

        "Marques",

        sorted(df["brand"].unique()),

        default=list(df["brand"].unique())

    )



with col2:

    transmissions = st.multiselect(

        "Transmission",

        sorted(df["transmission"].unique()),

        default=list(df["transmission"].unique())

    )



with col3:

    years = st.slider(

        "Année",

        int(df["year"].min()),

        int(df["year"].max()),

        (

            int(df["year"].min()),

            int(df["year"].max())

        )

    )




filtered = df[

    (df["brand"].isin(brands))

    &

    (df["transmission"].isin(transmissions))

    &

    (df["year"].between(
        years[0],
        years[1]
    ))

]



st.info(
    f"{len(filtered)} véhicules après filtrage"
)



st.divider()



# =====================================================
# TABLEAU
# =====================================================


st.header(
    "Données filtrées"
)


st.dataframe(

    filtered,

    use_container_width=True

)



st.divider()



# =====================================================
# GRAPHIQUES
# =====================================================


st.header(
    "Visualisations"
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
        "Prix FCFA"
    )


    ax.set_ylabel(
        "Nombre véhicules"
    )


    st.pyplot(fig)



# Marques

with col2:


    st.subheader(
        "Top marques"
    )


    brand_count = (

        filtered["brand"]

        .value_counts()

        .head(10)

    )


    fig,ax = plt.subplots()


    ax.bar(

        brand_count.index,

        brand_count.values

    )


    ax.set_xlabel(
        "Marques"
    )


    ax.set_ylabel(
        "Nombre"
    )


    plt.xticks(
        rotation=45
    )


    st.pyplot(fig)



st.divider()



# =====================================================
# ANALYSE ANNEE
# =====================================================


st.subheader(
    "Evolution des annonces par année"
)



year_count = (

    filtered["year"]

    .value_counts()

    .sort_index()

)



fig,ax = plt.subplots()



ax.plot(

    year_count.index,

    year_count.values,

    marker="o"

)


ax.set_xlabel(
    "Année"
)


ax.set_ylabel(
    "Nombre annonces"
)



st.pyplot(fig)



st.divider()



# =====================================================
# TOP PRIX
# =====================================================


st.header(
    "Véhicules les plus chers"
)



top = (

    filtered

    .sort_values(
        "price",
        ascending=False
    )

    [

        [

        "title",

        "brand",

        "model",

        "year",

        "price",

        "mileage"

        ]

    ]

    .head(10)

)



st.dataframe(

    top,

    use_container_width=True

)