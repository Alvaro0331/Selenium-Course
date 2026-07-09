from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def wrongCredentials(driver):
    try:
        #Find the username field using XPATH and enter a wrong username
        usernameField=driver.find_element(by=By.XPATH, value="//*[@id='username']")
        usernameField.send_keys("wrongUsername")
        time.sleep(1)
        #Find the password field using XPATH and enter a wrong password
        passwordField=driver.find_element(by=By.XPATH, value="//*[@id='password']")
        passwordField.send_keys("wrongPassword")
        time.sleep(1)
        #Find the login button using XPATH and click it
        loginButton=driver.find_element(by=By.XPATH, value="//*[@id='login']/button")
        loginButton.click()
        time.sleep(2)
    except Exception as e:
        print(f"An error occurred: {e}")


def correctCredentials(driver):
    #Find the username field using XPATH and enter the correct username
    usernameField=driver.find_element(by=By.XPATH, value="//*[@id='username']")
    usernameField.send_keys("tomsmith")
    time.sleep(1)
    #Find the password field using XPATH and enter the correct password
    passwordField=driver.find_element(by=By.XPATH, value="//*[@id='password']")
    passwordField.send_keys("SuperSecretPassword!")
    time.sleep(1)
    #Find the login button using XPATH and click it
    loginButton=driver.find_element(by=By.XPATH, value="//*[@id='login']/button")
    loginButton.click()
    time.sleep(2)
    #Find the logout button using XPATH and click it
    logoutButton=driver.find_element(by=By.XPATH, value="//*[@id='content']/div/a")
    logoutButton.click()
    time.sleep(2)


def main():
    driver = webdriver.Edge()
    driver.get("https://the-internet.herokuapp.com/login")
    
    if option == 'wrong':
        wrongCredentials(driver)
    else:
        correctCredentials(driver)

    driver.quit()






if __name__ == "__main__":
    option = 'correct'  # 'wrong' or 'correct'
    main()