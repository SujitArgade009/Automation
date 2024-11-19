import time
from itertools import dropwhile
from logging import exception
from re import search

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import time
from dotenv import load_dotenv
import os

load_dotenv()
email = os.getenv('POSTMAN_EMAIL')
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
search_input.send_keys("https://identity.getpostman.com/login")

#Will hit to postman page will insert the records
search_input.send_keys(Keys.RETURN)

#Will pause the operation for 15 sec and make use of the time sleeps
time.sleep(5)

#Will get the new page and will click on that page
try:
    postman_link= driver.find_element(By.XPATH,"//h3[contains(text(), 'Postman')]")
    postman_link.click()

except exception as BAD_LINK:
    print("the link cannot able to open and redirect to that page",BAD_LINK)

#fill the credentials
try:
    # Open the YouTube URL
    driver.get("https://identity.getpostman.com/login")
    driver.maximize_window()

    # Locate the email input field and enter the email address
    email_field = driver.find_element(By.CSS_SELECTOR, ".input-field.pm-form-control")
    email_field.send_keys(email)

    #locate the Password field and enter the password
    password_field  =driver.find_element(By.NAME,"password")
    password_field.send_keys(password)

    #Here Will check the credentials Manually
    time.sleep(8)

finally:
    driver.quit()