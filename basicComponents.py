from selenium import webdriver
from selenium.webdriver.common.by import By

#Start the session
driver= webdriver.Edge()

#Take action in browser
driver.get("https://www.selenium.dev/selenium/web/web-form.html")

#Request browser information
title = driver.title

#Establish waiting strategy
driver.implicitly_wait(0.5)

#Find an element
text_box= driver.find_element(by=By.NAME, value="my-text")
submit_button= driver.find_element(by=By.CSS_SELECTOR, value="button")

#Take action on element
text_box.send_keys("Selenium")
submit_button.click()

#Request element information
message= driver.find_element(by=By.ID, value="message")
text= message.text

#End the session
driver.quit()