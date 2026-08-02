import pandas as pd

from database.database import SessionLocal, engine, Base
from database.models import Book


CSV_FILE = "data/cleaned/books_clean.csv"



def import_books():

    print("==============================")
    print(" IMPORT BOOKS DATABASE ")
    print("==============================")


    Base.metadata.create_all(
        bind=engine
    )


    df = pd.read_csv(
        CSV_FILE
    )


    db = SessionLocal()


    try:

        count = 0


        for _, row in df.iterrows():


            book = Book(

                title=row.get("title"),

                price=row.get("price"),

                availability=row.get("availability"),

                rating=row.get("rating"),

                image=row.get("image"),

                description=row.get("description")

            )


            db.add(book)

            count += 1



        db.commit()


        print(
            "Nombre livres importés:",
            count
        )



    except Exception as e:


        db.rollback()

        print(
            "ERREUR:",
            e
        )


    finally:

        db.close()



if __name__ == "__main__":

    import_books()