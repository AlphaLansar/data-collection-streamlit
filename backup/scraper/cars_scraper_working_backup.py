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

    options.page_load_strategy = "eager"


    driver = webdriver.Chrome(
        service=Service(
            ChromeDriverManager().install()
        ),
        options=options
    )


    driver.set_page_load_timeout(
        60
    )


    return driver





# =====================================================
# UTILITAIRES
# =====================================================

def clean_text(text):

    if not text:

        return ""

    return (
        text
        .replace("\n"," ")
        .strip()
    )




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




def extract_brand_model(title):

    if not title:

        return "", ""


    parts = title.split()


    if parts and re.match(
        r"(19|20)\d{2}",
        parts[0]
    ):

        parts = parts[1:]


    if len(parts)==0:

        return "", ""


    brand = parts[0]


    model = " ".join(
        parts[1:]
    )


    return brand, model





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





    # URL

    try:

        link = card.find_element(
            By.XPATH,
            "./ancestor::a"
        )


        car["url"] = link.get_attribute(
            "href"
        )


    except:

        pass





    # TITRE

    try:

        title = card.find_element(
            By.CSS_SELECTOR,
            "h4"
        ).get_attribute(
            "title"
        )


        car["title"] = title


        brand, model = extract_brand_model(
            title
        )


        car["brand"] = brand

        car["model"] = model

        car["year"] = extract_year(
            title
        )


    except:

        pass





    # LOCATION

    try:

        location = card.find_element(
            By.CSS_SELECTOR,
            ".location"
        ).text


        car["location"] = clean_text(
            location
        )


        car["region"] = car["location"]


    except:

        pass





    # PRICE

    try:

        car["price"] = clean_text(
            card.find_element(
                By.CSS_SELECTOR,
                ".price"
            ).text
        )


    except:

        pass





    # MILEAGE

    try:

        mileage = card.find_element(
            By.CSS_SELECTOR,
            ".ad-vehicle-mileage .value"
        ).text


        mileage = (
            mileage
            .replace(
                "km",
                ""
            )
            .replace(
                "KM",
                ""
            )
            .replace(
                " ",
                ""
            )
        )


        car["mileage"] = mileage



    except:

        pass





    # ENGINE + FUEL

    try:

        engine_box = card.find_element(
            By.CSS_SELECTOR,
            ".engine-capacity"
        )


        spans = engine_box.find_elements(
            By.TAG_NAME,
            "span"
        )


        values=[]


        for span in spans:

            txt = clean_text(
                span.text
            )

            if txt:

                values.append(
                    txt
                )



        if len(values)>0:

            car["engine"] = values[0]



        if len(values)>1:

            car["fuel"] = (
                values[1]
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





    # TRANSMISSION

    try:

        car["transmission"] = clean_text(
            card.find_element(
                By.CSS_SELECTOR,
                ".transmission span"
            ).text
        )


    except:

        pass





    # STATUS

    try:

        car["status"] = clean_text(
            card.find_element(
                By.CSS_SELECTOR,
                ".ribbon"
            ).text
        )


    except:

        pass




    return car





# =====================================================
# SCRAPER
# =====================================================

def scrape_cars(pages):


    driver = create_driver()


    cars=[]



    try:


        for page in range(
            1,
            pages+1
        ):


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


                car = extract_card(
                    card
                )


                cars.append(
                    car
                )



    finally:

        driver.quit()



    return cars





# =====================================================
# CSV
# =====================================================

def save_csv(data):


    os.makedirs(
        "data/raw",
        exist_ok=True
    )


    df = pd.DataFrame(
        data
    )


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

if __name__ == "__main__":


    parser = argparse.ArgumentParser()


    parser.add_argument(
        "--pages",
        type=int,
        default=1
    )


    args = parser.parse_args()



    cars = scrape_cars(
        args.pages
    )


    save_csv(
        cars
    )