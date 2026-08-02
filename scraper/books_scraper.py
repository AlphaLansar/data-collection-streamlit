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

    driver = webdriver.Chrome(
        service=Service(
            ChromeDriverManager().install()
        ),
        options=options
    )

    return driver



def clean_price(price):

    try:

        price = price.replace(
            "£",
            ""
        )

        return float(price.strip())

    except:

        return None




def scrape_books(pages):


    os.makedirs(
        "data/raw",
        exist_ok=True
    )


    driver = create_driver()


    books=[]



    try:

        for page in range(1,pages+1):


            print(
                f"Scraping page {page}"
            )


            url = (
                f"https://books.toscrape.com/catalogue/page-{page}.html"
            )


            driver.get(url)



            WebDriverWait(
                driver,
                10
            ).until(
                EC.presence_of_element_located(
                    (
                        By.CSS_SELECTOR,
                        "article.product_pod"
                    )
                )
            )



            cards = driver.find_elements(
                By.CSS_SELECTOR,
                "article.product_pod"
            )



            products_count = len(cards)



            print(
                "Livres trouvés:",
                products_count
            )



            for card in cards:


                book={}



                # titre

                book["title"] = card.find_element(
                    By.CSS_SELECTOR,
                    "h3 a"
                ).get_attribute(
                    "title"
                )



                # prix

                price = card.find_element(
                    By.CSS_SELECTOR,
                    ".price_color"
                ).text


                book["price"] = clean_price(price)




                # disponibilité

                book["availability"] = card.find_element(
                    By.CSS_SELECTOR,
                    ".availability"
                ).text.strip()



                # nombre produits page

                book["products_count"] = products_count




                # note

                rating_class = card.find_element(
                    By.CSS_SELECTOR,
                    "p.star-rating"
                ).get_attribute(
                    "class"
                )


                book["rating"] = rating_class.replace(
                    "star-rating",
                    ""
                ).strip()




                # url détail

                detail_url = card.find_element(
                    By.CSS_SELECTOR,
                    "h3 a"
                ).get_attribute(
                    "href"
                )


                old_page = driver.current_url


                driver.get(
                    detail_url
                )


                time.sleep(0.5)



                # description

                try:

                    book["description"] = driver.find_element(
                        By.CSS_SELECTOR,
                        "#product_description ~ p"
                    ).text


                except:

                    book["description"]=""



                # catégorie

                try:

                    book["product_type"] = driver.find_elements(
                        By.CSS_SELECTOR,
                        "ul.breadcrumb li"
                    )[2].text


                except:

                    book["product_type"]=""



                # reviews

                try:

                    table_rows = driver.find_elements(
                        By.CSS_SELECTOR,
                        "table.table.table-striped tr"
                    )


                    reviews=""


                    for row in table_rows:

                        if "Number of reviews" in row.text:

                            reviews=row.find_elements(
                                By.TAG_NAME,
                                "td"
                            )[0].text


                    book["reviews"]=reviews


                except:

                    book["reviews"]=""




                # tax

                try:

                    rows = driver.find_elements(
                        By.CSS_SELECTOR,
                        "table.table.table-striped tr"
                    )


                    tax=""


                    for row in rows:

                        if "Tax" in row.text:

                            tax=row.find_elements(
                                By.TAG_NAME,
                                "td"
                            )[0].text


                    book["tax"]=tax


                except:

                    book["tax"]=""



                books.append(
                    book
                )



                driver.back()


                WebDriverWait(
                    driver,
                    10
                ).until(
                    EC.presence_of_element_located(
                        (
                            By.CSS_SELECTOR,
                            "article.product_pod"
                        )
                    )
                )



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

        writer.writerows(
            data
        )





if __name__=="__main__":


    parser = argparse.ArgumentParser()


    parser.add_argument(
        "--pages",
        type=int,
        default=5
    )


    args=parser.parse_args()



    books = scrape_books(
        args.pages
    )



    save_csv(
        books
    )


    print("======================")

    print(
        "CSV créé avec succès"
    )


    print(
        "Nombre livres:",
        len(books)
    )

    print("======================")