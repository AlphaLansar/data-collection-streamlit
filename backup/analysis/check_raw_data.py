import pandas as pd


FILE = "data/raw/cars.csv"


def main():

    print("==============================")
    print("      DATA QUALITY CHECK")
    print("==============================")

    df = pd.read_csv(FILE)


    print("\n1) Dimensions dataset")
    print("--------------------")
    print(df.shape)


    print("\n2) Colonnes")
    print("--------------------")

    for col in df.columns:
        print("-", col)



    print("\n3) Types des données")
    print("--------------------")

    print(df.dtypes)



    print("\n4) Valeurs manquantes")
    print("--------------------")

    print(df.isnull().sum())



    print("\n5) Doublons")
    print("--------------------")

    print(
        "Nombre doublons:",
        df.duplicated().sum()
    )



    print("\n6) Aperçu données")
    print("--------------------")

    print(
        df.head(10).to_string()
    )



    print("\n7) Statistiques")
    print("--------------------")

    print(
        df.describe(include="all")
    )


if __name__ == "__main__":
    main()