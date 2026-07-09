from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import logging

logging.basicConfig(level=logging.INFO)


def main():
    driver=webdriver.Edge()
    driver.get("https://the-internet.herokuapp.com/login")

    #Find the username field using XPATH and enter the correct username
    usernameField=driver.find_element(by=By.XPATH, value="//*[@id='username']")
    usernameField.send_keys("tomsmith")
    time.sleep(1)
    #Find the password field using XPATH and enter the correct password
    passwordField=driver.find_element(by=By.XPATH, value="//*[@id='password']")
    passwordField.send_keys("SuperSecretPassword")
    time.sleep(1)
    #Find the login button using XPATH and click it
    loginButton=driver.find_element(by=By.XPATH, value="//*[@id='login']/button")
    loginButton.click()
    time.sleep(2)

    #Check if login was successful
    try:
        successMessage=driver.find_element(by=By.CLASS_NAME, value="flash success")
        logging.info("Login successful.")
    except Exception as e:
        logging.error("Login failed")



if __name__ == "__main__":
    main()