import pandas as pd
import os


INPUT_FILE = "data/raw/cars.csv"
OUTPUT_FILE = "data/cleaned/cars_clean.csv"


print("==============================")
print(" CLEANING CARS DATA ")
print("==============================")


# ==========================
# Chargement
# ==========================

df = pd.read_csv(INPUT_FILE)


print("Dataset brut :", df.shape)



# ==========================
# Colonnes retenues
# Critères dashboard
# ==========================

columns = [
    "url",
    "title",
    "brand",
    "model",
    "year",
    "location",
    "region",
    "price",
    "mileage",
    "transmission"
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
        .fillna("Inconnu")
        .astype(str)
        .str.strip()
    )



# ==========================
# Nettoyage prix
# ==========================

df["price"] = (
    df["price"]
    .astype(str)
    .str.replace(
        r"[^\d]",
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
# Nettoyage mileage
# ==========================

df["mileage"] = (
    df["mileage"]
    .astype(str)
    .str.replace(
        r"[^\d]",
        "",
        regex=True
    )
)


df["mileage"] = pd.to_numeric(
    df["mileage"],
    errors="coerce"
)


df["mileage"] = df["mileage"].fillna(
    df["mileage"].median()
)



# ==========================
# Nettoyage année
# ==========================

df["year"] = pd.to_numeric(
    df["year"],
    errors="coerce"
)


df["year"] = df["year"].fillna(
    df["year"].median()
)


df["year"] = df["year"].astype(int)



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
# Types finaux
# ==========================

df["price"] = df["price"].astype(float)

df["mileage"] = df["mileage"].astype(int)

df["year"] = df["year"].astype(int)



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



print()
print("==============================")
print("NETTOYAGE TERMINE")
print("==============================")

print(
    "Dataset final :",
    df.shape
)


print()

print(
    "Colonnes finales :"
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
    "Statistiques prix :"
)

print(
    df["price"].describe()
)


print()

print(
    "Fichier généré :",
    OUTPUT_FILE
)


print("==============================")