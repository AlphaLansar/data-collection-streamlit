import streamlit as st
import pandas as pd
import plotly.express as px


st.set_page_config(
    page_title="Cars Analytics",
    layout="wide"
)



st.title(
    "Cars Analytics Dashboard"
)


st.write(
"""
Interactive exploration of the Gaaraas Cars dataset.

The dataset used in this dashboard comes from the Selenium
scraping pipeline after cleaning and preprocessing.
"""
)



FILE = "data/cleaned/cars_clean.csv"



@st.cache_data
def load_data():

    return pd.read_csv(FILE)



try:

    df = load_data()


except Exception as e:

    st.error(
        f"Unable to load dataset: {e}"
    )

    st.stop()



# ==========================
# FILTERS
# ==========================


st.sidebar.header(
    "Dataset Filters"
)



search = st.sidebar.text_input(
    "Search vehicle"
)



brands = st.sidebar.multiselect(
    "Brand",
    sorted(df["brand"].unique()),
    default=sorted(df["brand"].unique())
)



transmissions = st.sidebar.multiselect(
    "Transmission",
    sorted(df["transmission"].unique()),
    default=sorted(df["transmission"].unique())
)



regions = st.sidebar.multiselect(
    "Region",
    sorted(df["region"].unique()),
    default=sorted(df["region"].unique())
)



year_range = st.sidebar.slider(
    "Year range",
    int(df.year.min()),
    int(df.year.max()),
    (
        int(df.year.min()),
        int(df.year.max())
    )
)



filtered = df[

    (df["brand"].isin(brands))

    &

    (df["transmission"].isin(transmissions))

    &

    (df["region"].isin(regions))

    &

    (df["year"].between(
        year_range[0],
        year_range[1]
    ))

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
    "Vehicles",
    len(filtered)
)



c2.metric(
    "Average price",
    f"{filtered.price.mean():,.0f} FCFA"
)



c3.metric(
    "Brands",
    filtered.brand.nunique()
)



c4.metric(
    "Average mileage",
    f"{filtered.mileage.mean():,.0f} km"
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

    title="Vehicle price distribution"

)



st.plotly_chart(
    fig_price,
    use_container_width=True
)



# ==========================
# BRAND ANALYSIS
# ==========================


st.header(
    "Brand Analysis"
)



brand_df = (
    filtered["brand"]
    .value_counts()
    .reset_index()
)



brand_df.columns = [
    "brand",
    "count"
]



fig_brand = px.bar(

    brand_df,

    x="brand",

    y="count",

    title="Number of vehicles by brand"

)



st.plotly_chart(
    fig_brand,
    use_container_width=True
)



# ==========================
# YEAR / PRICE
# ==========================


st.header(
    "Price evolution according to year"
)



fig_year = px.scatter(

    filtered,

    x="year",

    y="price",

    size="mileage",

    color="brand",

    hover_data=[
        "model",
        "transmission"
    ],

    title="Vehicle price vs year"

)



st.plotly_chart(
    fig_year,
    use_container_width=True
)



# ==========================
# TRANSMISSION
# ==========================


st.header(
    "Transmission Analysis"
)



trans_df = (
    filtered["transmission"]
    .value_counts()
    .reset_index()
)



trans_df.columns = [
    "transmission",
    "count"
]



fig_trans = px.pie(

    trans_df,

    names="transmission",

    values="count",

    title="Transmission distribution"

)



st.plotly_chart(
    fig_trans,
    use_container_width=True
)



# ==========================
# TABLE
# ==========================


st.header(
    "Vehicle Details"
)



st.dataframe(

    filtered[
        [
            "brand",
            "model",
            "year",
            "price",
            "mileage",
            "transmission",
            "region"
        ]
    ],

    use_container_width=True

)



# ==========================
# DOWNLOAD
# ==========================


csv = filtered.to_csv(
    index=False
).encode(
    "utf-8"
)



st.download_button(

    label="Download filtered dataset",

    data=csv,

    file_name="cars_filtered.csv",

    mime="text/csv"

)



st.caption(
"""
Alpha DataLab - Cars Analytics Module
"""
)