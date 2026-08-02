import os
import pandas as pd


INPUT_FILE = "data/raw/cars.csv"

OUTPUT_FILE = "data/cleaned/cars_clean.csv"



def clean_price(value):

    if pd.isna(value):
        return None


    value = str(value)


    value = (
        value
        .replace("CFA","")
        .replace(" ","")
        .strip()
    )


    try:

        return int(value)

    except:

        return None





def clean_year(value):

    try:

        return int(value)

    except:

        return None





def clean_text(value):

    if pd.isna(value):

        return "Unknown"


    value = str(value).strip()


    if value == "":

        return "Unknown"


    return value





def main():


    print("==============================")
    print(" CLEANING CARS DATA ")
    print("==============================")


    df = pd.read_csv(
        INPUT_FILE
    )


    print("Avant nettoyage:")
    print(df.shape)



    # suppression doublons

    df = df.drop_duplicates()



    # suppression colonnes inutiles

    useless_columns = [

        "fuel",
        "engine",
        "status"

    ]


    df = df.drop(
        columns=useless_columns,
        errors="ignore"
    )



    # prix numérique

    df["price"] = df["price"].apply(
        clean_price
    )



    # année

    df["year"] = df["year"].apply(
        clean_year
    )



    # textes

    text_columns = [

        "url",
        "title",
        "brand",
        "model",
        "location",
        "region",
        "transmission"

    ]



    for col in text_columns:

        df[col] = df[col].apply(
            clean_text
        )



    # création dossier

    os.makedirs(
        "data/cleaned",
        exist_ok=True
    )



    df.to_csv(
        OUTPUT_FILE,
        index=False,
        encoding="utf-8"
    )



    print("\nAprès nettoyage:")
    print(df.shape)


    print("\nFichier créé:")
    print(
        OUTPUT_FILE
    )


    print("==============================")





if __name__ == "__main__":

    main()