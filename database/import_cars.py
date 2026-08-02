import pandas as pd

from database.database import SessionLocal, engine, Base
from database.models import Car


CSV_FILE = "data/cleaned/cars_clean.csv"


def import_cars():

    print("==============================")
    print(" IMPORT CARS DATABASE ")
    print("==============================")


    Base.metadata.create_all(bind=engine)


    df = pd.read_csv(CSV_FILE)


    db = SessionLocal()

    try:

        count = 0

        for _, row in df.iterrows():

            car = Car(
                url=row.get("url"),
                title=row.get("title"),
                brand=row.get("brand"),
                model=row.get("model"),
                year=row.get("year"),
                location=row.get("location"),
                region=row.get("region"),
                price=row.get("price"),
                mileage=row.get("mileage"),
                transmission=row.get("transmission")
            )


            db.add(car)
            count += 1


        db.commit()


        print(
            "Nombre voitures importées:",
            count
        )


    except Exception as e:

        db.rollback()

        print("ERREUR:", e)


    finally:

        db.close()



if __name__ == "__main__":
    import_cars()