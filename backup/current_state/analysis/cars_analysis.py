import os
import pandas as pd
import matplotlib.pyplot as plt


# =====================================================
# CONFIGURATION
# =====================================================

INPUT_FILE = "data/cleaned/cars_clean.csv"


FIGURE_DIR = "reports/cars/figures"

STAT_DIR = "reports/cars/statistics"


os.makedirs(
    FIGURE_DIR,
    exist_ok=True
)

os.makedirs(
    STAT_DIR,
    exist_ok=True
)


# =====================================================
# CHARGEMENT DATA
# =====================================================

print("==============================")
print(" CARS EXPLORATORY ANALYSIS ")
print("==============================")


df = pd.read_csv(INPUT_FILE)


print("\nDataset chargé:")
print(df.shape)



# =====================================================
# PREPARATION
# =====================================================


df["price"] = pd.to_numeric(
    df["price"],
    errors="coerce"
)


df["mileage"] = pd.to_numeric(
    df["mileage"],
    errors="coerce"
)


df["year"] = pd.to_numeric(
    df["year"],
    errors="coerce"
)



# =====================================================
# STATISTIQUES GENERALES
# =====================================================


statistics = []


statistics.append(
    "Nombre total véhicules : "
    + str(len(df))
)


statistics.append(
    "Prix moyen : "
    + str(round(df["price"].mean(),2))
    + " FCFA"
)


statistics.append(
    "Prix minimum : "
    + str(df["price"].min())
    + " FCFA"
)


statistics.append(
    "Prix maximum : "
    + str(df["price"].max())
    + " FCFA"
)


statistics.append(
    "Kilométrage moyen : "
    + str(round(df["mileage"].mean(),2))
    + " km"
)


statistics.append(
    "Année moyenne : "
    + str(round(df["year"].mean(),2))
)



statistics.append(
    "\nTransmission dominante : "
    + str(
        df["transmission"]
        .value_counts()
        .idxmax()
    )
)



statistics.append(
    "\nMarques principales :"
)


for brand,count in (
    df["brand"]
    .value_counts()
    .head(10)
    .items()
):

    statistics.append(
        f"{brand} : {count}"
    )




# sauvegarde statistiques

with open(
    f"{STAT_DIR}/cars_statistics.txt",
    "w",
    encoding="utf-8"
) as file:

    file.write(
        "\n".join(statistics)
    )


print("\nStatistiques sauvegardées")



# =====================================================
# GRAPHIQUES
# =====================================================


# 1 Distribution prix


plt.figure(figsize=(10,6))


plt.hist(
    df["price"],
    bins=20
)


plt.title(
    "Distribution des prix des véhicules"
)


plt.xlabel(
    "Prix FCFA"
)


plt.ylabel(
    "Nombre véhicules"
)


plt.savefig(
    f"{FIGURE_DIR}/price_distribution.png",
    bbox_inches="tight"
)


plt.close()



# 2 Top marques


brands = (
    df["brand"]
    .value_counts()
    .head(10)
)



plt.figure(figsize=(10,6))


plt.bar(
    brands.index,
    brands.values
)


plt.title(
    "Top 10 marques automobiles"
)


plt.xlabel(
    "Marque"
)


plt.ylabel(
    "Nombre annonces"
)


plt.xticks(
    rotation=45
)


plt.savefig(
    f"{FIGURE_DIR}/top_brands.png",
    bbox_inches="tight"
)


plt.close()




# 3 Transmission


transmission = (
    df["transmission"]
    .value_counts()
)



plt.figure(figsize=(7,5))


plt.bar(
    transmission.index,
    transmission.values
)


plt.title(
    "Répartition des transmissions"
)


plt.xlabel(
    "Transmission"
)


plt.ylabel(
    "Nombre annonces"
)


plt.savefig(
    f"{FIGURE_DIR}/transmission_distribution.png",
    bbox_inches="tight"
)


plt.close()




# 4 Kilométrage


plt.figure(figsize=(10,6))


plt.hist(
    df["mileage"],
    bins=20
)


plt.title(
    "Distribution du kilométrage"
)


plt.xlabel(
    "Kilométrage (km)"
)


plt.ylabel(
    "Nombre véhicules"
)



plt.savefig(
    f"{FIGURE_DIR}/mileage_distribution.png",
    bbox_inches="tight"
)


plt.close()




# 5 Année vs prix


plt.figure(figsize=(10,6))


plt.scatter(
    df["year"],
    df["price"]
)



plt.title(
    "Relation année du véhicule et prix"
)


plt.xlabel(
    "Année"
)


plt.ylabel(
    "Prix FCFA"
)



plt.savefig(
    f"{FIGURE_DIR}/year_price_relation.png",
    bbox_inches="tight"
)


plt.close()



print("\n==============================")
print(" ANALYSE TERMINEE ")
print("==============================")