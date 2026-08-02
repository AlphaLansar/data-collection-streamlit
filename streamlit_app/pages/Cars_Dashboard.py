import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


st.set_page_config(
    page_title="Cars Dashboard",
    layout="wide"
)


st.title("🚗 Dashboard - Annonces automobiles Gaaraas")



FILE = "data/cleaned/cars_clean.csv"



@st.cache_data
def load_data():

    return pd.read_csv(FILE)



df = load_data()



st.success(
    f"Dataset chargé : {df.shape[0]} voitures"
)



# ==========================
# INFORMATIONS GENERALES
# ==========================


st.header("📌 Informations générales")



col1, col2, col3, col4 = st.columns(4)



with col1:

    st.metric(
        "Nombre voitures",
        len(df)
    )



with col2:

    st.metric(
        "Prix moyen",
        f"{df['price'].mean():,.0f} FCFA"
    )



with col3:

    st.metric(
        "Kilométrage moyen",
        f"{df['mileage'].mean():,.0f} KM"
    )



with col4:

    st.metric(
        "Marques",
        df["brand"].nunique()
    )



st.divider()



# ==========================
# FILTRES
# ==========================


st.sidebar.header("Filtres")



brands = st.sidebar.multiselect(

    "Marque",

    df["brand"].unique()

)



transmission = st.sidebar.multiselect(

    "Transmission",

    df["transmission"].unique()

)



filtered=df.copy()



if brands:

    filtered = filtered[
        filtered["brand"].isin(brands)
    ]



if transmission:

    filtered = filtered[
        filtered["transmission"].isin(transmission)
    ]





st.subheader("📋 Données filtrées")


st.dataframe(

    filtered,

    use_container_width=True

)



st.divider()



# ==========================
# VISUALISATIONS
# ==========================



st.header("📊 Analyse des données")



col1,col2 = st.columns(2)



with col1:


    st.subheader(
        "Nombre d'annonces par marque"
    )


    fig,ax=plt.subplots()


    filtered["brand"].value_counts().plot(

        kind="bar",

        ax=ax

    )


    ax.set_xlabel("Marque")

    ax.set_ylabel("Nombre")


    st.pyplot(fig)




with col2:


    st.subheader(
        "Distribution des prix"
    )


    fig,ax=plt.subplots()


    ax.hist(

        filtered["price"],

        bins=20

    )


    ax.set_xlabel(
        "Prix FCFA"
    )


    ax.set_ylabel(
        "Nombre voitures"
    )


    st.pyplot(fig)




# ==========================
# RELATION PRIX ANNEE
# ==========================


st.subheader(
    "Relation année - prix"
)



fig,ax=plt.subplots()



ax.scatter(

    filtered["year"],

    filtered["price"]

)



ax.set_xlabel(
    "Année"
)


ax.set_ylabel(
    "Prix FCFA"
)



st.pyplot(fig)





st.divider()



st.info(
"""
Variables analysées :

✅ Marque  
✅ Modèle  
✅ Année  
✅ Prix  
✅ Kilométrage  
✅ Type de boîte  
✅ Région de vente  

Conforme aux variables demandées dans le cahier des charges.
"""
)