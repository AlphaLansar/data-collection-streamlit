import os
import sys
import pandas as pd


# Ajouter la racine du projet au PATH Python
ROOT_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

sys.path.append(ROOT_DIR)


from database.database import SessionLocal, engine, Base
from database.models import Book


CSV_FILE = "data/cleaned/books_clean.csv"


print("==============================")
print(" IMPORT BOOKS INTO SQLITE ")
print("==============================")


# Création tables
Base.metadata.create_all(
    bind=engine
)


# Chargement CSV

df = pd.read_csv(
    CSV_FILE
)


print(
    "Livres à importer:",
    len(df)
)


db = SessionLocal()


try:

    # éviter doublons
    db.query(Book).delete()


    for _, row in df.iterrows():

        book = Book(

            title=row["title"],

            price=float(
                row["price"]
            ),

            availability=row["availability"],

            rating=str(
                row["rating"]
            ),

            description=row["description"]

        )


        db.add(book)


    db.commit()


    print("==============================")
    print("IMPORT TERMINE")
    print(
        "Nombre livres:",
        len(df)
    )
    print("==============================")


except Exception as e:

    db.rollback()

    print(
        "Erreur:",
        e
    )


finally:

    db.close()