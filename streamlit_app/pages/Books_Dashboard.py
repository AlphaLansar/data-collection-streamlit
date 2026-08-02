import streamlit as st
import pandas as pd
import plotly.express as px


st.set_page_config(
    page_title="Books Analytics",
    layout="wide"
)


st.title(
    "Books Analytics Dashboard"
)


st.write(
"""
Exploration interactive du dataset Books To Scrape.

Les données utilisées proviennent du pipeline Selenium
après nettoyage et preprocessing.
"""
)


FILE = "data/cleaned/books_clean.csv"



@st.cache_data
def load_data():

    return pd.read_csv(FILE)



df = load_data()



# ==========================
# SIDEBAR FILTERS
# ==========================


st.sidebar.header(
    "Dataset Filters"
)



search = st.sidebar.text_input(
    "Search by title"
)



ratings = st.sidebar.multiselect(
    "Rating",
    sorted(df["rating"].unique()),
    default=sorted(df["rating"].unique())
)



categories = st.sidebar.multiselect(
    "Category",
    sorted(df["product_type"].unique()),
    default=sorted(df["product_type"].unique())
)



filtered = df[
    (df["rating"].isin(ratings))
    &
    (df["product_type"].isin(categories))
]



if search:

    filtered = filtered[
        filtered["title"]
        .str.contains(
            search,
            case=False,
            na=False
        )
    ]



# ==========================
# KPI
# ==========================


st.header(
    "Dataset Overview"
)


c1,c2,c3,c4 = st.columns(4)


c1.metric(
    "Total books",
    len(filtered)
)


c2.metric(
    "Average price",
    f"{filtered.price.mean():.2f}"
)


c3.metric(
    "Highest price",
    f"{filtered.price.max():.2f}"
)


c4.metric(
    "Categories",
    filtered.product_type.nunique()
)



st.divider()



# ==========================
# PRICE ANALYSIS
# ==========================


st.header(
    "Price Analysis"
)


fig_price = px.histogram(
    filtered,
    x="price",
    nbins=20,
    title="Book price distribution"
)


st.plotly_chart(
    fig_price,
    use_container_width=True
)



# ==========================
# RATING ANALYSIS
# ==========================


st.header(
    "Rating Analysis"
)


rating_df = (
    filtered["rating"]
    .value_counts()
    .reset_index()
)


rating_df.columns = [
    "rating",
    "count"
]



fig_rating = px.bar(
    rating_df,
    x="rating",
    y="count",
    title="Books by rating"
)



st.plotly_chart(
    fig_rating,
    use_container_width=True
)



# ==========================
# CATEGORY ANALYSIS
# ==========================


st.header(
    "Category Distribution"
)



cat_df = (
    filtered["product_type"]
    .value_counts()
    .reset_index()
)


cat_df.columns = [
    "category",
    "count"
]



fig_cat = px.bar(
    cat_df,
    x="category",
    y="count",
    title="Books by category"
)



st.plotly_chart(
    fig_cat,
    use_container_width=True
)



# ==========================
# TABLE
# ==========================


st.header(
    "Books Details"
)



st.dataframe(
    filtered[
        [
            "title",
            "price",
            "availability",
            "rating",
            "product_type"
        ]
    ],
    use_container_width=True
)



# ==========================
# DOWNLOAD
# ==========================


csv = filtered.to_csv(
    index=False
).encode("utf-8")



st.download_button(
    label="Download filtered dataset",
    data=csv,
    file_name="books_filtered.csv",
    mime="text/csv"
)



st.caption(
"""
Alpha DataLab - Books Analytics Module
"""
)