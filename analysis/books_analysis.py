import os
import pandas as pd
import matplotlib.pyplot as plt


# ==============================
# CONFIGURATION
# ==============================

INPUT_FILE = "data/cleaned/books_clean.csv"

FIG_DIR = "reports/books/figures"

STAT_DIR = "reports/books/statistics"


os.makedirs(
    FIG_DIR,
    exist_ok=True
)


os.makedirs(
    STAT_DIR,
    exist_ok=True
)



# ==============================
# CHARGEMENT
# ==============================


print("==============================")
print(" BOOKS DATA ANALYSIS ")
print("==============================")


df = pd.read_csv(INPUT_FILE)


print("\nDataset chargé:")
print(df.shape)



# ==============================
# PREPARATION
# ==============================


df["price"] = pd.to_numeric(
    df["price"],
    errors="coerce"
)



# ==============================
# STATISTIQUES
# ==============================


stats = []


stats.append(
    f"Nombre total livres : {len(df)}"
)


stats.append(
    f"Prix moyen : {round(df['price'].mean(),2)}"
)


stats.append(
    f"Prix médian : {df['price'].median()}"
)


stats.append(
    f"Prix minimum : {df['price'].min()}"
)


stats.append(
    f"Prix maximum : {df['price'].max()}"
)



# disponibilité


availability = (
    df["availability"]
    .value_counts()
)


stats.append(
    "\nDisponibilité:"
)


for k,v in availability.items():

    stats.append(
        f"{k}: {v}"
    )



# rating


rating = (
    df["rating"]
    .value_counts()
)


stats.append(
    "\nRatings:"
)


for k,v in rating.items():

    stats.append(
        f"{k}: {v}"
    )



with open(
    STAT_DIR + "/books_statistics.txt",
    "w",
    encoding="utf-8"
) as f:

    for s in stats:
        f.write(s+"\n")



print("Statistiques sauvegardées")



# ==============================
# GRAPHIQUES
# ==============================



# 1 Distribution prix


plt.figure(
    figsize=(10,6)
)


plt.hist(
    df["price"],
    bins=20
)


plt.title(
    "Distribution des prix des livres"
)


plt.xlabel(
    "Prix"
)


plt.ylabel(
    "Nombre de livres"
)


plt.savefig(
    FIG_DIR+"/books_price_distribution.png",
    bbox_inches="tight"
)


plt.close()




# 2 Rating


rating_counts = (
    df["rating"]
    .value_counts()
)


plt.figure(
    figsize=(8,5)
)


rating_counts.plot(
    kind="bar"
)


plt.title(
    "Répartition des ratings"
)


plt.xlabel(
    "Rating"
)


plt.ylabel(
    "Nombre"
)


plt.savefig(
    FIG_DIR+"/books_rating_distribution.png",
    bbox_inches="tight"
)


plt.close()




# 3 Disponibilité


availability_counts = (
    df["availability"]
    .value_counts()
)



plt.figure(
    figsize=(8,5)
)


availability_counts.plot(
    kind="bar"
)


plt.title(
    "Disponibilité des livres"
)


plt.xlabel(
    "Disponibilité"
)


plt.ylabel(
    "Nombre"
)


plt.savefig(
    FIG_DIR+"/books_availability.png",
    bbox_inches="tight"
)


plt.close()




# 4 Top 10 livres chers


top_books = (
    df.sort_values(
        "price",
        ascending=False
    )
    .head(10)
)



plt.figure(
    figsize=(10,6)
)


plt.barh(
    top_books["title"],
    top_books["price"]
)


plt.title(
    "Top 10 livres les plus chers"
)


plt.xlabel(
    "Prix"
)


plt.ylabel(
    "Livre"
)


plt.gca().invert_yaxis()


plt.savefig(
    FIG_DIR+"/books_top_expensive.png",
    bbox_inches="tight"
)


plt.close()



print("==============================")
print(" ANALYSE TERMINEE ")
print("==============================")