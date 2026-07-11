from selenium import webdriver
from selenium.webdriver.common.by import By
import logging
import csv

logging.basicConfig(level=logging.INFO)

savedData= []

#Read the data from the CSV file
def read_csv():
    try:
        with open("./Data-DrivenTest/books.csv", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                savedData.append(row)
        logging.info("CSV data read successfully.")
    except FileNotFoundError:
        logging.error("CSV file not found.")


def main():
    read_csv()

    driver = webdriver.Edge()
    try:
        currentData = []
        #Loop through the pages
        for page in range(1,2):
            if page == 1:
                driver.get("https://books.toscrape.com/")
            else:
                driver.get(f"https://books.toscrape.com/catalogue/page-{page}.html")

            #Find all the books elements
            books = driver.find_elements(by=By.CSS_SELECTOR, value="article.product_pod")

            #Extract title and price for each book and store it in currentData
            for book in books:
                titleElement = book.find_element(by=By.CSS_SELECTOR, value="h3 a")
                title = titleElement.get_attribute("title")

                priceElement = book.find_element(by=By.CSS_SELECTOR, value="p.price_color")
                price = priceElement.text

                currentData.append({"Title":title, "Price":price})
    
        #Compare current data with saved data
        discrepancies = []
        
        for savedBook in savedData:
            currentBook =next(
                (book for book in currentData if book["Title"] == savedBook["Title"]),
                None
            )

            if currentBook:
                if currentBook["Price"] != savedBook["Price"]:
                    discrepancies.append({
                        "Title": savedBook["Title"],
                        "SavedPrice": savedBook["Price"],
                        "CurrentPrice": currentBook["Price"]
                    })
                    logging.error(f"Price discrepancy found for {savedBook['Title']}: Saved price = {savedBook['Price']}, Current Price = {currentBook["Price"]}")
                else:
                    logging.info(f"Price verified correctly for {savedBook["Title"]}: {savedBook["Price"]}")
            else:
                logging.error(f"Book no found on the website: {savedBook["Title"]}")
            

            #Save discrepancies on CSV
            if discrepancies:
                fieldNames=["Title", "SavedPrice", "CurrentPrice"]
                with open("./Data-DrivenTest/price_discrepancies.csv", "w", newline="", encoding="utf-8") as file:
                    writer = csv.DictWriter(file, fieldnames=fieldNames)
                    writer.writeheader()
                    writer.writerows(discrepancies)
                    logging.info("Disrepancies saved in CSV file")
            else:
                logging.info("No price discrepancies found")
                
                
                



    except Exception as e:
        logging.error(f"An error has occurred: {e}")
    finally:
        driver.quit()
    



if __name__ == "__main__":
    main()