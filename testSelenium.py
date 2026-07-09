#Launch the Edge browser and open the URL

from selenium import webdriver

driver = webdriver.Edge()
driver.get("https://selenium.dev")
driver.quit()