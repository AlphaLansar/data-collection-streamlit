import os
import re
import time
import argparse
import pandas as pd


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

from selenium.common.exceptions import TimeoutException

from webdriver_manager.chrome import ChromeDriverManager



BASE_URL = "https://www.gaaraas.com/fr/users/dakar-auto?page={}"

OUTPUT_FILE = "data/raw/cars.csv"



# =====================================================
# DRIVER
# =====================================================

def create_driver():

    options = Options()

    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")

    options.add_argument(
        "--window-size=1920,1080"
    )


    # chargement rapide
    options.page_load_strategy = "eager"


    driver = webdriver.Chrome(
        service=Service(
            ChromeDriverManager().install()
        ),
        options=options
    )


    driver.set_page_load_timeout(60)


    return driver



# =====================================================
# UTILITAIRES
# =====================================================


def extract_brand_model(title):

    if not title:
        return "", ""


    parts = title.split()


    if parts[0].isdigit():

        parts = parts[1:]


    if len(parts)==0:

        return "",""



    brand = parts[0]


    model = " ".join(
        parts[1:]
    )


    return brand,model




def extract_year(title):

    if not title:
        return ""


    result = re.search(
        r"(19|20)\d{2}",
        title
    )


    if result:

        return result.group()


    return ""





# =====================================================
# EXTRACTION CARTE
# =====================================================


def extract_card(card):


    car = {

        "url":"",
        "title":"",
        "brand":"",
        "model":"",
        "year":"",
        "location":"",
        "region":"",
        "price":"",
        "mileage":"",
        "fuel":"",
        "transmission":"",
        "engine":"",
        "status":""

    }



    # titre

    try:

        title = card.find_element(
            By.CSS_SELECTOR,
            "h4"
        ).get_attribute(
            "title"
        )


        car["title"]=title


        car["brand"], car["model"] = extract_brand_model(title)


        car["year"] = extract_year(title)


    except:

        pass





    # localisation

    try:

        car["location"] = card.find_element(
            By.CSS_SELECTOR,
            ".location"
        ).text


        car["region"]=car["location"]


    except:

        pass





    # prix

    try:

        price = card.find_element(
            By.CSS_SELECTOR,
            ".price"
        ).text


        car["price"]=price.replace(
            " ",
            ""
        )


    except:

        pass






    # kilometrage

    try:

        mileage = card.find_element(
            By.CSS_SELECTOR,
            ".ad-vehicle-mileage .value"
        ).text


        car["mileage"] = (
            mileage
            .replace("KM","")
            .replace("km","")
            .replace(" ","")
            .strip()
        )


    except:

        pass






    # moteur + carburant

    try:

        engine = card.find_element(
            By.CSS_SELECTOR,
            ".engine-capacity"
        )


        spans = engine.find_elements(
            By.TAG_NAME,
            "span"
        )


        if len(spans)>0:

            car["engine"] = spans[0].text



        if len(spans)>1:

            car["fuel"] = (
                spans[1]
                .text
                .replace(
                    "(",
                    ""
                )
                .replace(
                    ")",
                    ""
                )
                .strip()
            )


    except:

        pass






    # transmission

    try:

        car["transmission"] = card.find_element(
            By.CSS_SELECTOR,
            ".transmission span"
        ).text


    except:

        pass






    # statut

    try:

        car["status"] = card.find_element(
            By.CSS_SELECTOR,
            ".ribbon"
        ).text


    except:

        pass




    return car





# =====================================================
# SCRAPER PRINCIPAL
# =====================================================


def scrape_cars(pages):


    driver=create_driver()


    cars=[]


    try:


        for page in range(1,pages+1):


            print()
            print(
                "Scraping page",
                page
            )


            try:

                driver.get(
                    BASE_URL.format(page)
                )


            except TimeoutException:

                print(
                    "Timeout page",
                    page
                )

                continue




            time.sleep(3)



            cards = driver.find_elements(
                By.CSS_SELECTOR,
                ".ad-specification"
            )



            print(
                "Voitures trouvées:",
                len(cards)
            )



            for card in cards:


                try:

                    car = extract_card(card)

                    cars.append(car)


                except Exception as e:

                    print(
                        "Erreur carte:",
                        e
                    )




    finally:

        driver.quit()



    return cars





# =====================================================
# SAUVEGARDE CSV
# =====================================================


def save_csv(data):


    os.makedirs(
        "data/raw",
        exist_ok=True
    )


    df=pd.DataFrame(data)



    df.to_csv(
        OUTPUT_FILE,
        index=False,
        encoding="utf-8"
    )



    print()
    print("======================")
    print(
        "CSV créé avec succès"
    )
    print(
        "Nombre voitures:",
        len(df)
    )
    print("======================")





# =====================================================
# MAIN
# =====================================================


if __name__=="__main__":


    parser=argparse.ArgumentParser()


    parser.add_argument(
        "--pages",
        type=int,
        default=1
    )


    args=parser.parse_args()



    data=scrape_cars(
        args.pages
    )


    save_csv(data)