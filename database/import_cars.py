import os
import sys
import pandas as pd


ROOT_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

sys.path.append(ROOT_DIR)



from database.database import SessionLocal, engine, Base
from database.models import Car



CSV_FILE = "data/cleaned/cars_clean.csv"



print("==============================")
print(" IMPORT CARS INTO SQLITE ")
print("==============================")



Base.metadata.create_all(
    bind=engine
)



df = pd.read_csv(
    CSV_FILE
)



print(
    "Voitures à importer:",
    len(df)
)



db = SessionLocal()



try:


    db.query(Car).delete()



    for _, row in df.iterrows():


        car = Car(

            url=row["url"],

            title=row["title"],

            brand=row["brand"],

            model=row["model"],

            year=int(
                row["year"]
            ),

            location=row["location"],

            region=row["region"],

            price=int(
                row["price"]
            ),

            mileage=int(
                row["mileage"]
            ),

            transmission=row["transmission"]

        )


        db.add(car)



    db.commit()



    print("==============================")
    print("IMPORT TERMINE")
    print(
        "Nombre voitures:",
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