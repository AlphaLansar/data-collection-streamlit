import os
import pandas as pd
import matplotlib.pyplot as plt


INPUT_FILE = "data/cleaned/cars_clean.csv"

FIG_DIR = "reports/cars/figures"

STAT_DIR = "reports/cars/statistics"


os.makedirs(
    FIG_DIR,
    exist_ok=True
)

os.makedirs(
    STAT_DIR,
    exist_ok=True
)



print("==============================")
print(" CARS DATA ANALYSIS ")
print("==============================")


df = pd.read_csv(INPUT_FILE)


print("Dataset chargé:", df.shape)



# =========================
# STATISTIQUES
# =========================


stats = []


stats.append(
    f"Nombre voitures: {len(df)}"
)


stats.append(
    f"Prix moyen: {df['price'].mean():.2f}"
)


stats.append(
    f"Prix maximum: {df['price'].max()}"
)


stats.append(
    f"Prix minimum: {df['price'].min()}"
)


stats.append(
    f"Kilométrage moyen: {df['mileage'].mean():.2f}"
)


stats.append(
    f"Nombre marques: {df['brand'].nunique()}"
)



with open(
    STAT_DIR + "/cars_statistics.txt",
    "w",
    encoding="utf-8"
) as f:

    for s in stats:
        f.write(s + "\n")



# =========================
# Prix distribution
# =========================


plt.figure(figsize=(8,5))

plt.hist(
    df["price"],
    bins=15
)

plt.title(
    "Distribution des prix des voitures"
)

plt.xlabel(
    "Prix FCFA"
)

plt.ylabel(
    "Nombre voitures"
)


plt.savefig(
    FIG_DIR + "/price_distribution.png",
    bbox_inches="tight"
)

plt.close()



# =========================
# Kilométrage
# =========================


plt.figure(figsize=(8,5))

plt.hist(
    df["mileage"],
    bins=15
)


plt.title(
    "Distribution kilométrage"
)

plt.xlabel(
    "Kilométrage"
)


plt.ylabel(
    "Nombre voitures"
)


plt.savefig(
    FIG_DIR + "/mileage_distribution.png",
    bbox_inches="tight"
)


plt.close()



# =========================
# Marques
# =========================


plt.figure(figsize=(8,5))


df["brand"].value_counts().plot(
    kind="bar"
)


plt.title(
    "Top marques automobiles"
)


plt.xlabel(
    "Marque"
)


plt.ylabel(
    "Nombre"
)



plt.xticks(
    rotation=45
)


plt.savefig(
    FIG_DIR + "/top_brands.png",
    bbox_inches="tight"
)


plt.close()



# =========================
# Transmission
# =========================


plt.figure(figsize=(8,5))


df["transmission"].value_counts().plot(
    kind="bar"
)



plt.title(
    "Types de transmission"
)



plt.savefig(
    FIG_DIR + "/transmission_distribution.png",
    bbox_inches="tight"
)



plt.close()



# =========================
# Année / Prix
# =========================


plt.figure(figsize=(8,5))


plt.scatter(
    df["year"],
    df["price"]
)



plt.title(
    "Relation année et prix"
)


plt.xlabel(
    "Année"
)


plt.ylabel(
    "Prix FCFA"
)


plt.savefig(
    FIG_DIR + "/year_price_relation.png",
    bbox_inches="tight"
)


plt.close()



print("Statistiques sauvegardées")


print("==============================")
print(" ANALYSE TERMINEE ")
print("==============================")