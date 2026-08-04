import os
import csv
import time
import argparse

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.common.by import By

from webdriver_manager.chrome import ChromeDriverManager



OUTPUT_FILE = "data/raw/books.csv"

BASE_URL = (
    "https://books.toscrape.com/catalogue/page-{}.html"
)



# ==========================
# DRIVER
# ==========================

def create_driver():

    options = Options()

    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")


    return webdriver.Chrome(
        service=Service(
            ChromeDriverManager().install()
        ),
        options=options
    )



# ==========================
# UTILITAIRES
# ==========================

def clean_price(price):

    try:

        return float(
            price
            .replace("£","")
            .strip()
        )

    except:

        return None



# ==========================
# DETAIL LIVRE
# ==========================

def extract_details(driver,url):


    book={}


    driver.get(url)

    time.sleep(1)



    try:

        book["title"] = driver.find_element(
            By.CSS_SELECTOR,
            "div.product_main h1"
        ).text


    except:

        book["title"]=""



    try:

        book["price"] = clean_price(
            driver.find_element(
                By.CSS_SELECTOR,
                ".price_color"
            ).text
        )


    except:

        book["price"]=None



    try:

        book["availability"] = driver.find_element(
            By.CSS_SELECTOR,
            ".availability"
        ).text.strip()


    except:

        book["availability"]=""



    try:

        rating = driver.find_element(
            By.CSS_SELECTOR,
            "p.star-rating"
        ).get_attribute(
            "class"
        )


        book["rating"] = (
            rating
            .replace(
                "star-rating",
                ""
            )
            .strip()
        )


    except:

        book["rating"]=""



    try:

        book["description"] = driver.find_element(
            By.CSS_SELECTOR,
            "#product_description ~ p"
        ).text


    except:

        book["description"]=""



    book["product_type"]=""

    book["reviews"]=""

    book["tax"]=""



    try:

        rows = driver.find_elements(
            By.CSS_SELECTOR,
            "table.table.table-striped tr"
        )


        for row in rows:

            text=row.text


            if "Product Type" in text:

                book["product_type"]=row.find_elements(
                    By.TAG_NAME,
                    "td"
                )[0].text


            if "Number of reviews" in text:

                book["reviews"]=row.find_elements(
                    By.TAG_NAME,
                    "td"
                )[0].text


            if "Tax" in text:

                book["tax"]=row.find_elements(
                    By.TAG_NAME,
                    "td"
                )[0].text


    except:

        pass



    book["url"]=url


    return book



# ==========================
# SCRAPER TOUTES LES PAGES
# ==========================

def scrape_books(pages=None):


    os.makedirs(
        "data/raw",
        exist_ok=True
    )


    driver=create_driver()


    books=[]


    page=1



    try:


        while True:


            if pages and page > pages:

                break



            print(
                "Scraping page",
                page
            )


            driver.get(
                BASE_URL.format(page)
            )


            cards = driver.find_elements(
                By.CSS_SELECTOR,
                "article.product_pod"
            )



            print(
                "Livres trouvés:",
                len(cards)
            )



            if len(cards)==0:

                print(
                    "Fin des pages"
                )

                break



            links=[]


            for card in cards:


                link=card.find_element(
                    By.CSS_SELECTOR,
                    "h3 a"
                ).get_attribute(
                    "href"
                )


                links.append(link)



            for link in links:


                book=extract_details(
                    driver,
                    link
                )


                book["products_count"]=len(cards)


                books.append(book)



            page+=1



    finally:

        driver.quit()



    return books



# ==========================
# CSV
# ==========================

def save_csv(data):


    with open(
        OUTPUT_FILE,
        "w",
        newline="",
        encoding="utf-8"
    ) as f:


        writer=csv.DictWriter(
            f,
            fieldnames=data[0].keys()
        )


        writer.writeheader()

        writer.writerows(data)




# ==========================
# MAIN
# ==========================

if __name__=="__main__":


    parser=argparse.ArgumentParser()


    parser.add_argument(
        "--pages",
        type=int,
        default=None
    )


    args=parser.parse_args()



    books=scrape_books(
        args.pages
    )


    save_csv(
        books
    )


    print("======================")
    print("CSV créé avec succès")
    print(
        "Nombre livres:",
        len(books)
    )
    print("======================")