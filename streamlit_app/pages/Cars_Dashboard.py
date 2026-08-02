import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os


st.set_page_config(
    page_title="Cars Analytics Dashboard",
    layout="wide"
)


st.title(
    "Cars Analytics Dashboard"
)


st.write(
"""
Analyse interactive des annonces automobiles collectées
depuis Gaaraas avec Selenium WebDriver.

Pipeline :
Scraping Selenium → Nettoyage Pandas → Analyse → Dashboard
"""
)


# =====================================================
# CHEMIN DATASET
# =====================================================

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
    "cars_clean.csv"
)


# =====================================================
# CHARGEMENT
# =====================================================


@st.cache_data
def load_data():

    df = pd.read_csv(FILE)

    return df



df = load_data()



# =====================================================
# VERIFICATION DATASET
# =====================================================


required_columns = [
    "brand",
    "model",
    "year",
    "price",
    "mileage",
    "transmission",
    "region"
]


missing = [
    col for col in required_columns
    if col not in df.columns
]


if missing:

    st.error(
        "Mauvaises données chargées"
    )


    st.write(
        "Colonnes attendues :"
    )


    st.write(required_columns)


    st.write(
        "Colonnes trouvées :"
    )


    st.write(
        df.columns.tolist()
    )


    st.stop()



st.success(
    f"Dataset chargé : {len(df)} véhicules"
)



# =====================================================
# INDICATEURS
# =====================================================


st.header(
    "Indicateurs principaux"
)



col1,col2,col3,col4 = st.columns(4)


with col1:

    st.metric(
        "Nombre véhicules",
        len(df)
    )


with col2:

    st.metric(
        "Prix moyen",
        f"{df['price'].mean():,.0f} FCFA"
    )


with col3:

    st.metric(
        "Marques",
        df["brand"].nunique()
    )


with col4:

    st.metric(
        "Kilométrage moyen",
        f"{df['mileage'].mean():,.0f}"
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
        "Marque",
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



st.write(
    f"Résultat : {len(filtered)} véhicules"
)



# =====================================================
# TABLE
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



with col1:

    st.subheader(
        "Distribution des prix"
    )


    fig,ax = plt.subplots()


    ax.hist(
        filtered["price"],
        bins=15
    )


    ax.set_xlabel(
        "Prix FCFA"
    )


    ax.set_ylabel(
        "Nombre"
    )


    st.pyplot(fig)



with col2:

    st.subheader(
        "Top marques"
    )


    brand_count = (
        filtered["brand"]
        .value_counts()
    )


    fig,ax = plt.subplots()


    ax.bar(
        brand_count.index,
        brand_count.values
    )


    ax.set_xlabel(
        "Marque"
    )


    ax.set_ylabel(
        "Nombre"
    )


    plt.xticks(
        rotation=45
    )


    st.pyplot(fig)



col3,col4 = st.columns(2)



with col3:

    st.subheader(
        "Kilométrage"
    )


    fig,ax = plt.subplots()


    ax.hist(
        filtered["mileage"],
        bins=15
    )


    st.pyplot(fig)



with col4:

    st.subheader(
        "Transmission"
    )


    transmission = (
        filtered["transmission"]
        .value_counts()
    )


    fig,ax = plt.subplots()


    ax.bar(
        transmission.index,
        transmission.values
    )


    st.pyplot(fig)



st.divider()



# =====================================================
# EXPORT
# =====================================================


st.header(
    "Export"
)



csv = filtered.to_csv(
    index=False
)


st.download_button(
    "Télécharger CSV",
    csv,
    "cars_filtered.csv",
    "text/csv"
)



st.caption(
"""
Projet Data Collection
Alpha Abdoulaye Lansar
Selenium | Pandas | SQL | Streamlit
"""
)