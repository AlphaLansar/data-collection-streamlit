import os
import csv
import argparse
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from webdriver_manager.chrome import ChromeDriverManager


OUTPUT_FILE = "data/raw/books.csv"


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


def clean_price(price):

    try:
        return float(
            price.replace("£", "").strip()
        )

    except:
        return None



def scrape_books(pages=None):

    os.makedirs(
        "data/raw",
        exist_ok=True
    )

    driver = create_driver()

    books = []

    page = 1


    try:

        while True:


            if pages and page > pages:
                break


            print(
                f"Scraping page {page}"
            )


            url = (
                f"https://books.toscrape.com/catalogue/page-{page}.html"
            )


            driver.get(url)



            cards = driver.find_elements(
                By.CSS_SELECTOR,
                "article.product_pod"
            )


            if not cards:
                print("Fin des pages")
                break



            print(
                "Livres trouvés:",
                len(cards)
            )



            for card in cards:


                book = {}



                book["title"] = card.find_element(
                    By.CSS_SELECTOR,
                    "h3 a"
                ).get_attribute(
                    "title"
                )


                price = card.find_element(
                    By.CSS_SELECTOR,
                    ".price_color"
                ).text


                book["price"] = clean_price(price)



                book["availability"] = card.find_element(
                    By.CSS_SELECTOR,
                    ".availability"
                ).text.strip()



                book["products_count"] = len(cards)



                rating = card.find_element(
                    By.CSS_SELECTOR,
                    "p.star-rating"
                ).get_attribute(
                    "class"
                )


                book["rating"] = rating.replace(
                    "star-rating",
                    ""
                ).strip()



                detail_url = card.find_element(
                    By.CSS_SELECTOR,
                    "h3 a"
                ).get_attribute(
                    "href"
                )


                driver.get(detail_url)


                try:
                    book["description"] = driver.find_element(
                        By.CSS_SELECTOR,
                        "#product_description ~ p"
                    ).text

                except:

                    book["description"] = ""



                try:

                    book["product_type"] = driver.find_elements(
                        By.CSS_SELECTOR,
                        "ul.breadcrumb li"
                    )[2].text

                except:

                    book["product_type"] = ""



                try:

                    rows = driver.find_elements(
                        By.CSS_SELECTOR,
                        "table.table.table-striped tr"
                    )

                    for row in rows:

                        if "Number of reviews" in row.text:

                            book["reviews"] = row.find_elements(
                                By.TAG_NAME,
                                "td"
                            )[0].text


                except:

                    book["reviews"] = ""



                try:

                    rows = driver.find_elements(
                        By.CSS_SELECTOR,
                        "table.table.table-striped tr"
                    )

                    for row in rows:

                        if "Tax" in row.text:

                            book["tax"] = row.find_elements(
                                By.TAG_NAME,
                                "td"
                            )[0].text


                except:

                    book["tax"] = ""



                books.append(book)



                driver.back()



            page += 1



    finally:

        driver.quit()



    return books




def save_csv(data):

    with open(
        OUTPUT_FILE,
        "w",
        newline="",
        encoding="utf-8"
    ) as f:


        writer = csv.DictWriter(
            f,
            fieldnames=data[0].keys()
        )

        writer.writeheader()
        writer.writerows(data)




if __name__ == "__main__":


    parser = argparse.ArgumentParser()


    parser.add_argument(
        "--pages",
        type=int,
        default=None
    )


    args = parser.parse_args()



    books = scrape_books(
        args.pages
    )


    save_csv(
        books
    )


    print("======================")
    print("CSV créé avec succès")
    print("Nombre livres:", len(books))
    print("======================")