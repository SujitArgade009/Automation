from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import  Keys
import time
from dotenv import load_dotenv
import os

load_dotenv()
email = os.getenv('POSTMAN_EMAIL')
password = os.getenv('POSTMAN_PASSWORD')

# Define the path to ChromeDriver
chromedriver_path = "C:\\Users\\SUJIT ARGADE\\Downloads\\chromedriver-win32\\chromedriver-win32\\chromedriver.exe"

# Set up the service object for ChromeDriver
service = Service(executable_path=chromedriver_path)

# Initialize the WebDriver
driver = webdriver.Chrome(service=service)

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

    # Pause for CAPTCHA
    input("Please complete the CAPTCHA manually and press Enter to continue...")

    # Press Enter or click the login button
    #password_field.send_keys(Keys.RETURN)
    # login into the postman
    login_field = driver.find_element(By.__class__, "btn btn-primary sign-in-btn")
    login_field.click()

    # Wait to ensure the login is successful
    time.sleep(20)

finally:
    # Cleanup: Close the browser
    driver.quit()
