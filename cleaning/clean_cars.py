import pandas as pd
import os


INPUT_FILE = "data/raw/cars.csv"
OUTPUT_FILE = "data/cleaned/cars_clean.csv"


print("==============================")
print(" CLEANING CARS DATA ")
print("==============================")


# Chargement
df = pd.read_csv(INPUT_FILE)


print("Avant nettoyage:", df.shape)



# ==========================
# Colonnes examen professeur
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
# Nettoyage texte
# ==========================

for col in df.select_dtypes(include="object").columns:

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
        " ",
        "",
        regex=False
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
# Nettoyage kilométrage
# ==========================

df["mileage"] = (
    df["mileage"]
    .astype(str)
    .str.replace(
        " ",
        "",
        regex=False
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

df = df.drop_duplicates()



# ==========================
# Sauvegarde
# ==========================

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

print("Valeurs manquantes:")
print(df.isnull().sum())


print()

print("Statistiques prix:")
print(df["price"].describe())


print()

print("Fichier créé:")
print(OUTPUT_FILE)


print("==============================")