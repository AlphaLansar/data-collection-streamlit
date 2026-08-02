import streamlit as st
import pandas as pd
import os


st.set_page_config(
    page_title="No-Code Web Scraper",
    page_icon="🧩",
    layout="wide"
)


st.title(
    "🧩 Données brutes - Web Scraper (No-Code)"
)


st.write(
"""
Cette section permet de télécharger les données
brutes collectées avec l'outil no-code Web Scraper
(extension Chrome).

Les fichiers ne subissent aucun nettoyage.
"""
)


st.divider()



DATA_PATH = "data/nocode"



st.header(
    "📚 Books To Scrape - Web Scraper"
)



books_file = os.path.join(
    DATA_PATH,
    "books_webscraper_raw.csv"
)



if os.path.exists(books_file):

    df_books = pd.read_csv(
        books_file
    )

    st.success(
        "Fichier disponible"
    )

    st.metric(
        "Nombre lignes",
        len(df_books)
    )

    st.dataframe(
        df_books.head(20),
        use_container_width=True
    )


    with open(
        books_file,
        "rb"
    ) as file:

        st.download_button(
            label="⬇️ Télécharger Books Web Scraper CSV",
            data=file,
            file_name="books_webscraper_raw.csv",
            mime="text/csv"
        )


else:

    st.info(
        """
        Aucun fichier disponible.

        Ajoutez :
        data/nocode/books_webscraper_raw.csv
        """
    )



st.divider()



st.header(
    "🚗 Gaaraas Cars - Web Scraper"
)



cars_file = os.path.join(
    DATA_PATH,
    "cars_webscraper_raw.csv"
)



if os.path.exists(cars_file):

    df_cars = pd.read_csv(
        cars_file
    )


    st.success(
        "Fichier disponible"
    )


    st.metric(
        "Nombre lignes",
        len(df_cars)
    )


    st.dataframe(
        df_cars.head(20),
        use_container_width=True
    )


    with open(
        cars_file,
        "rb"
    ) as file:

        st.download_button(
            label="⬇️ Télécharger Cars Web Scraper CSV",
            data=file,
            file_name="cars_webscraper_raw.csv",
            mime="text/csv"
        )


else:

    st.info(
        """
        Aucun fichier disponible.

        Ajoutez :
        data/nocode/cars_webscraper_raw.csv
        """
    )