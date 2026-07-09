from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def cssSelector(driver):
    try:
        element = driver.find_element(by=By.CSS_SELECTOR, value="#offers")
        element.click()
        time.sleep(3)  # Wait for 3 seconds to observe the result
        print("Clicked element using CSS selector.")
    except Exception as e:
        print(f"An error occurred: {e}")


def xpathSelector(driver):
    try:
        element = driver.find_element(by=By.XPATH, value="//*[@id='offers']")
        element.click()
        time.sleep(3)  # Wait for 3 seconds to observe the result
        print("Clicked element using XPATH selector.")
    except Exception as e:
        print(f"An error occurred: {e}")



def main():
    # Launch the Edge browser and open the URL
    driver = webdriver.Edge()
    driver.get("https://bstackdemo.com/")
    time.sleep(3)  # Wait for 3 seconds to observe the page load
    
    if option== 'css':
        cssSelector(driver)
    else:
        xpathSelector(driver)
    
    driver.quit()



if __name__ == "__main__":
    option = 'xpath' # 'css' or 'xpath'
    main()
