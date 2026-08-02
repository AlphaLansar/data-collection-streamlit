import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


st.set_page_config(
    page_title="Cars Dashboard",
    layout="wide"
)


st.title("🚗 Dashboard Analyse des voitures")


FILE = "data/cleaned/cars_clean.csv"



# ==========================
# Chargement
# ==========================

try:

    df = pd.read_csv(FILE)


except Exception as e:

    st.error(
        f"Erreur chargement données : {e}"
    )

    st.stop()



st.success(
    f"Données chargées : {len(df)} voitures"
)



st.divider()



# ==========================
# Informations générales
# ==========================


st.header("📊 Informations générales")


col1,col2,col3,col4 = st.columns(4)


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
        "Marques",
        df["brand"].nunique()
    )


with col4:

    st.metric(
        "Kilométrage moyen",
        f"{df['mileage'].mean():,.0f}"
    )



st.divider()



# ==========================
# Filtres
# ==========================


st.header("🔎 Filtres")


col1,col2,col3 = st.columns(3)



with col1:

    brands = st.multiselect(
        "Marque",
        df["brand"].unique(),
        default=df["brand"].unique()
    )



with col2:

    transmissions = st.multiselect(
        "Transmission",
        df["transmission"].unique(),
        default=df["transmission"].unique()
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
    f"Résultat : {len(filtered)} voitures"
)



st.dataframe(
    filtered,
    use_container_width=True
)



st.divider()



# ==========================
# Graphiques
# ==========================


st.header("📈 Visualisations")



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


    fig,ax = plt.subplots()


    filtered["brand"].value_counts().plot(
        kind="bar",
        ax=ax
    )


    ax.set_xlabel(
        "Marque"
    )


    ax.set_ylabel(
        "Nombre"
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


    fig,ax = plt.subplots()


    filtered["transmission"].value_counts().plot(
        kind="bar",
        ax=ax
    )


    st.pyplot(fig)



st.divider()



# ==========================
# Téléchargement
# ==========================


st.header("⬇️ Export données filtrées")


csv = filtered.to_csv(
    index=False
)


st.download_button(
    "Télécharger CSV",
    csv,
    "cars_filtered.csv",
    "text/csv"
)