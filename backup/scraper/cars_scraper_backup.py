import os
import time
import argparse
import pandas as pd


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

from webdriver_manager.chrome import ChromeDriverManager



BASE_URL = "https://www.gaaraas.com/fr/users/dakar-auto?page={}"

DOMAIN = "https://www.gaaraas.com"



# =====================================================
# DRIVER
# =====================================================

def create_driver():

    options = Options()

    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")


    driver = webdriver.Chrome(
        service=Service(
            ChromeDriverManager().install()
        ),
        options=options
    )


    return driver




# =====================================================
# EXTRACTION PROPRIETES
# =====================================================

def extract_properties(driver):

    data = {

        "mileage":"",
        "year":"",
        "color":"",
        "body_type":"",
        "fuel":"",
        "transmission":"",
        "engine":"",
        "air_conditioning":"",
        "steering":"",
        "condition":""

    }



    mapping = {

        "Kilométrage":"mileage",
        "Année":"year",
        "Couleur":"color",
        "Carrosserie":"body_type",
        "Carburant":"fuel",
        "Boîte de vitesses":"transmission",
        "Climatisation":"air_conditioning",
        "Volant":"steering",
        "Condition":"condition"

    }



    props = driver.find_elements(
        By.CSS_SELECTOR,
        ".prop"
    )


    for prop in props:

        try:

            spans = prop.find_elements(
                By.TAG_NAME,
                "span"
            )


            if len(spans) >= 2:

                key = spans[0].get_attribute(
                    "title"
                )

                value = spans[1].get_attribute(
                    "title"
                )


                if key in mapping:

                    data[mapping[key]]=value


        except:

            pass



    return data




# =====================================================
# DETAIL VEHICULE
# =====================================================

def scrape_detail(driver,url):


    driver.get(url)

    time.sleep(2)



    car={}


    car["url"]=url



    try:

        car["title"]=driver.find_element(
            By.CSS_SELECTOR,
            ".ad-title h2"
        ).text


    except:

        car["title"]=""




    try:

        car["location"]=driver.find_element(
            By.CSS_SELECTOR,
            ".ad-title a span"
        ).text


    except:

        car["location"]=""




    try:

        car["price"]=driver.find_element(
            By.CSS_SELECTOR,
            ".ad-price .price"
        ).text.replace(
            " ",
            ""
        )


    except:

        car["price"]=""



    car.update(
        extract_properties(driver)
    )



    try:

        car["status"]=driver.find_element(
            By.CSS_SELECTOR,
            ".ribbon"
        ).text


    except:

        car["status"]=""




    try:

        car["description"]=driver.find_element(
            By.CSS_SELECTOR,
            ".ad-seller-comment p"
        ).text


    except:

        car["description"]=""




    try:

        car["created_date"]=driver.find_element(
            By.CSS_SELECTOR,
            ".ad-created-border strong"
        ).text


    except:

        car["created_date"]=""



    return car





# =====================================================
# SCRAPER
# =====================================================

def scrape_cars(max_pages=100):


    driver=create_driver()


    cars=[]


    try:


        for page in range(1,max_pages+1):


            print()
            print(
                "Scraping page",
                page
            )


            driver.get(
                BASE_URL.format(page)
            )


            time.sleep(3)



            # liens annonces
            links = driver.find_elements(
                By.CSS_SELECTOR,
                "a[href*='/fr/ads/']"
            )



            print(
                "Annonces trouvées:",
                len(links)
            )



            if len(links)==0:

                break



            urls=[]



            for link in links:


                try:

                    href=link.get_attribute(
                        "href"
                    )


                    if href and href not in urls:

                        urls.append(
                            href
                        )


                except:

                    pass





            for i,url in enumerate(urls,1):


                print(
                    f"{i}/{len(urls)}"
                )


                try:


                    car=scrape_detail(
                        driver,
                        url
                    )


                    cars.append(
                        car
                    )


                    print(
                        car["title"]
                    )


                except Exception as e:

                    print(
                        "Erreur:",
                        e
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


    df=pd.DataFrame(data)



    columns=[

        "url",
        "title",
        "location",
        "price",
        "mileage",
        "year",
        "color",
        "body_type",
        "fuel",
        "transmission",
        "engine",
        "air_conditioning",
        "steering",
        "condition",
        "status",
        "created_date",
        "description"

    ]



    for c in columns:

        if c not in df.columns:

            df[c]=""



    df=df[columns]



    df.to_csv(
        "data/raw/cars.csv",
        index=False
    )


    print("==============================")
    print("CSV créé")
    print(
        "Nombre voitures:",
        len(df)
    )
    print("==============================")





# =====================================================
# MAIN
# =====================================================

if __name__=="__main__":


    parser=argparse.ArgumentParser()


    parser.add_argument(
        "--pages",
        type=int,
        default=100
    )


    args=parser.parse_args()



    cars=scrape_cars(
        args.pages
    )


    save_csv(cars)