import os
import pandas as pd


INPUT_FILE = "data/raw/books.csv"
OUTPUT_FILE = "data/cleaned/books_clean.csv"


print("==============================")
print(" CLEANING BOOKS DATA ")
print("==============================")


# ==========================
# Chargement
# ==========================

df = pd.read_csv(INPUT_FILE)


print("Dataset brut :", df.shape)



# ==========================
# Sélection colonnes utiles
# ==========================

columns = [
    "title",
    "price",
    "availability",
    "products_count",
    "rating",
    "description",
    "product_type",
    "reviews",
    "tax",
    "url"
]


df = df[
    [c for c in columns if c in df.columns]
]



# ==========================
# Suppression lignes vides
# ==========================

df = df.dropna(
    how="all"
)



# ==========================
# Nettoyage texte
# ==========================

text_columns = df.select_dtypes(
    include="object"
).columns


for col in text_columns:

    df[col] = (
        df[col]
        .fillna("Non disponible")
        .astype(str)
        .str.strip()
    )



# ==========================
# Prix
# ==========================

df["price"] = (
    df["price"]
    .astype(str)
    .str.replace(
        r"[^\d.]",
        "",
        regex=True
    )
)


df["price"] = pd.to_numeric(
    df["price"],
    errors="coerce"
)


df["price"] = df["price"].fillna(
    df["price"].median()
)



# ==========================
# Tax
# ==========================

df["tax"] = (
    df["tax"]
    .astype(str)
    .str.replace(
        r"[^\d.]",
        "",
        regex=True
    )
)


df["tax"] = pd.to_numeric(
    df["tax"],
    errors="coerce"
)


df["tax"] = df["tax"].fillna(0)



# ==========================
# Rating
# ==========================

rating_map = {

    "One":1,
    "Two":2,
    "Three":3,
    "Four":4,
    "Five":5

}


df["rating"] = df["rating"].map(
    rating_map
)



df["rating"] = df["rating"].fillna(
    0
).astype(int)



# ==========================
# Reviews
# ==========================

df["reviews"] = pd.to_numeric(
    df["reviews"],
    errors="coerce"
)


df["reviews"] = (
    df["reviews"]
    .fillna(0)
    .astype(int)
)



# ==========================
# Products count
# ==========================

df["products_count"] = pd.to_numeric(
    df["products_count"],
    errors="coerce"
)


df["products_count"] = (
    df["products_count"]
    .fillna(0)
    .astype(int)
)



# ==========================
# Suppression doublons
# ==========================

if "url" in df.columns:

    df = df.drop_duplicates(
        subset=["url"]
    )

else:

    df = df.drop_duplicates()



# ==========================
# Suppression url pour analyse
# ==========================

if "url" in df.columns:

    df.drop(
        columns=["url"],
        inplace=True
    )



# ==========================
# Export
# ==========================

os.makedirs(
    "data/cleaned",
    exist_ok=True
)


df.to_csv(
    OUTPUT_FILE,
    index=False,
    encoding="utf-8"
)



print("==============================")
print("NETTOYAGE TERMINE")
print("==============================")


print(
    "Dataset final :",
    df.shape
)


print()

print(
    "Colonnes :"
)

print(
    df.columns.tolist()
)


print()

print(
    "Valeurs manquantes :"
)

print(
    df.isnull().sum()
)


print()

print(
    "Fichier créé :",
    OUTPUT_FILE
)


print("==============================")