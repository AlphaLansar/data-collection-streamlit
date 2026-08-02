import os
import pandas as pd


INPUT_FILE = "data/raw/books.csv"
OUTPUT_FILE = "data/cleaned/books_clean.csv"



print("==============================")
print(" CLEANING BOOKS DATA ")
print("==============================")


df = pd.read_csv(INPUT_FILE)


print("Avant nettoyage:", df.shape)


# Nettoyage prix
df["price"] = (
    df["price"]
    .astype(str)
    .str.replace("£","", regex=False)
    .astype(float)
)


# Nettoyage availability
df["availability"] = (
    df["availability"]
    .astype(str)
    .str.replace("In stock", "In stock")
)


# Nettoyage rating
rating_map = {
    "One":1,
    "Two":2,
    "Three":3,
    "Four":4,
    "Five":5
}


df["rating"] = df["rating"].map(rating_map)



# Conversion reviews
df["reviews"] = (
    pd.to_numeric(
        df["reviews"],
        errors="coerce"
    )
    .fillna(0)
    .astype(int)
)



# Conversion tax
df["tax"] = (
    df["tax"]
    .astype(str)
    .str.replace("£","", regex=False)
    .astype(float)
)



# Suppression colonnes inutiles
for col in ["image","url"]:

    if col in df.columns:
        df.drop(
            columns=[col],
            inplace=True
        )



# Valeurs manquantes
df.fillna(
    {
        "description":"Non disponible",
        "product_type":"Unknown"
    },
    inplace=True
)



os.makedirs(
    "data/cleaned",
    exist_ok=True
)



df.to_csv(
    OUTPUT_FILE,
    index=False
)



print("Après nettoyage:", df.shape)

print()
print("Colonnes finales:")
print(df.columns.tolist())


print()
print("Fichier créé:")
print(OUTPUT_FILE)

print("==============================")