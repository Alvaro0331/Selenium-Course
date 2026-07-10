from selenium import webdriver
from selenium.webdriver.common.by import By


def main():
    driver = webdriver.Edge()
    
    try:
        driver.get("https://books.toscrape.com/")
        driver.implicitly_wait(5)

        #Arrays to store the scraped data
        titles = []
        prices = []

        #Loop through the pages
        for page in range (1, 2):

            #Find all the books elements
            books = driver.find_elements(by=By.CSS_SELECTOR, value="article.product_pod")

            #Loop through each book and extract the title and price
            for book in books:
                titleElement = book.find_element(by=By.CSS_SELECTOR, value="h3 a")
                title = titleElement.get_attribute("title")

                priceElement = book.find_element(by=By.CSS_SELECTOR, value="p.price_color")
                price = priceElement.text

                titles.append(title)
                prices.append(price)
            
            #Navigate to the next page
            if page < 2:
                nextButton = driver.find_element(by=By.CSS_SELECTOR, value="li.next a")
                nextButton.click()
        
        #Print the scraped data
        for i in range(len(titles)):
            print(f"Title: {titles[i]}, Price: {prices[i]}")
        
        #Save the results in a CSV file
        csvContent="Title,Price\n"
        for i in range(len(titles)):
            csvContent += f"{titles[i]},{prices[i]}\n"
        with open("./WebScraping/scraped_data.csv", "w") as file:
            file.write(csvContent)

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        driver.quit()



if __name__ == "__main__":
    main()