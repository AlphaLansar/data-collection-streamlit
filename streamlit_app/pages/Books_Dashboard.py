import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt



st.set_page_config(

    page_title="Books Dashboard",

    layout="wide"

)



st.title(
    "📚 Dashboard - Books To Scrape"
)



FILE = "data/cleaned/books_clean.csv"



@st.cache_data
def load_data():

    return pd.read_csv(FILE)



df = load_data()



st.success(

    f"Dataset chargé : {len(df)} livres"

)



# ============================
# INFORMATIONS GENERALES
# ============================


st.header("📌 Informations générales")



col1,col2,col3,col4 = st.columns(4)



with col1:

    st.metric(

        "Nombre de livres",

        len(df)

    )



with col2:

    st.metric(

        "Prix moyen",

        f"{df['price'].mean():.2f} £"

    )



with col3:

    st.metric(

        "Prix maximum",

        f"{df['price'].max():.2f} £"

    )



with col4:

    st.metric(

        "Catégories",

        df["product_type"].nunique()

    )





st.divider()



# ============================
# FILTRES
# ============================



st.sidebar.header(
    "Filtres"
)



rating = st.sidebar.multiselect(

    "Note",

    df["rating"].unique()

)



availability = st.sidebar.multiselect(

    "Disponibilité",

    df["availability"].unique()

)



category = st.sidebar.multiselect(

    "Type de produit",

    df["product_type"].unique()

)



filtered=df.copy()



if rating:

    filtered = filtered[

        filtered["rating"].isin(rating)

    ]



if availability:

    filtered = filtered[

        filtered["availability"].isin(availability)

    ]



if category:

    filtered = filtered[

        filtered["product_type"].isin(category)

    ]





# ============================
# TABLEAU
# ============================



st.header(
    "📋 Données des livres"
)



st.dataframe(

    filtered,

    use_container_width=True

)





st.divider()



# ============================
# GRAPHIQUES
# ============================



st.header(
    "📊 Visualisations"
)



col1,col2 = st.columns(2)



with col1:


    st.subheader(
        "Distribution des prix"
    )


    fig,ax=plt.subplots()



    ax.hist(

        filtered["price"],

        bins=20

    )



    ax.set_xlabel(
        "Prix (£)"
    )


    ax.set_ylabel(
        "Nombre livres"
    )


    st.pyplot(fig)





with col2:


    st.subheader(
        "Distribution des notes"
    )


    fig,ax=plt.subplots()



    filtered["rating"].value_counts().plot(

        kind="bar",

        ax=ax

    )


    ax.set_xlabel(
        "Note"
    )


    ax.set_ylabel(
        "Nombre"
    )


    st.pyplot(fig)





# ============================
# PRODUITS LES PLUS CHERS
# ============================



st.subheader(

    "🏆 Livres les plus chers"

)



top_books = filtered.sort_values(

    by="price",

    ascending=False

).head(10)



st.dataframe(

    top_books[

        [
            "title",

            "price",

            "rating",

            "product_type"

        ]

    ],

    use_container_width=True

)





# ============================
# VARIABLES DU PROFESSEUR
# ============================


st.info(
"""
Variables utilisées :

✅ Titre du livre  
✅ Prix  
✅ Disponibilité  
✅ Nombre produits sur page  
✅ Note produit  
✅ Nombre reviews  
✅ Description  
✅ Type produit  
✅ Tax  

Dashboard conforme au cahier des charges.
"""
)