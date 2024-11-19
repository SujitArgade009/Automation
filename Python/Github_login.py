
from selenium import webdriver
from logging import exception
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import time
from dotenv import load_dotenv
import os

load_dotenv()
email = os.getenv('GITHUB_USERNAME')
password = os.getenv('POSTMAN_PASSWORD')

#define the path of the chrome ChromeDriver
chromedriver_path="C:\\Users\\SUJIT ARGADE\\Downloads\\chromedriver-win32\\chromedriver-win32\\chromedriver.exe"

# Set up the service object for ChromeDriver
service=Service(executable_path = chromedriver_path)

#Intilize the web-driver
driver=webdriver.Chrome(service=service)

#Open the Chrome
driver.get("https://www.google.com/")
driver.maximize_window()

#We will search postman.login page on Google
search_input=driver.find_element(By.NAME, value="q")
search_input.send_keys("https://github.com/login")

#Will hit to postman page will insert the records
search_input.send_keys(Keys.RETURN)

#Will pause the operation for 15 sec and make use of the time sleeps
time.sleep(5)

#Will get the new page and will click on that page
try:
    postman_link= driver.find_element(By.XPATH,"//h3[normalize-space()='Sign in to GitHub · GitHub']")
    postman_link.click()

except exception as BAD_LINK:
    print("the link cannot able to open and redirect to that page",BAD_LINK)

#fill the credentials
try:


    # Locate the email input field and enter the email address
    email_field = driver.find_element(By.ID, "login_field")
    email_field.send_keys(email)

    #locate the Password field and enter the password
    password_field  =driver.find_element(By.ID,"password")
    password_field.send_keys(password)

    #Click on sign in in page
    login_click=driver.find_element(By.NAME,"commit")
    login_click.click()
    print("Click successful")

    # Here Will check the credentials Manually
    time.sleep(8)

finally:
    print("UI Automation has been run successfully")
    time.sleep(3)
    driver.quit()