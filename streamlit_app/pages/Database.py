import streamlit as st
import sqlite3
import pandas as pd


st.set_page_config(
    page_title="Database Explorer",
    layout="wide"
)


st.title(
    "Database Explorer"
)


st.write(
"""
SQL database connected to the Data Collection platform.

The database stores cleaned data collected through Selenium scraping.
"""
)



DATABASE = "books_cars.db"



def get_tables():

    conn = sqlite3.connect(DATABASE)

    tables = pd.read_sql(
        """
        SELECT name 
        FROM sqlite_master
        WHERE type='table'
        """,
        conn
    )

    conn.close()

    return tables



def load_table(table):

    conn = sqlite3.connect(DATABASE)

    df = pd.read_sql(
        f"SELECT * FROM {table}",
        conn
    )

    conn.close()

    return df



if st.button(
    "Refresh database"
):

    st.cache_data.clear()



try:

    tables = get_tables()


    if len(tables)==0:

        st.warning(
            "No tables found. Import data into database first."
        )

        st.stop()



    st.success(
        "Database connected successfully"
    )



    st.header(
        "Available tables"
    )


    st.dataframe(
        tables,
        use_container_width=True
    )



    for table in tables["name"]:


        st.divider()


        st.subheader(
            f"Table : {table}"
        )


        df = load_table(table)


        c1,c2 = st.columns(2)


        c1.metric(
            "Rows",
            len(df)
        )


        c2.metric(
            "Columns",
            len(df.columns)
        )


        st.dataframe(
            df.head(10),
            use_container_width=True
        )



except Exception as e:


    st.error(
        f"Database error : {e}"
    )



st.caption(
"""
Alpha DataLab - SQL Database Module
"""
)