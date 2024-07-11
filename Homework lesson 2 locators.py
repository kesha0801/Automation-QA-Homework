from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# open the url
driver.get('https://www.amazon.com/')

# amazon logo
driver.find_element(By.XPATH, "//i[@aria-label='Amazon']")

# email field
driver.find_element(By.ID, 'ap_email')

# continue button
driver.find_element(By.ID, 'continue')

# Conditions of use link
driver.find_element(By.XPATH, "//a[text()='Conditions of Use']")

# Privacy Notice link
driver.find_element(By.XPATH, "//a[text()='Privacy Notice']")

# Need help link
driver.find_element(By.XPATH, "//span[@class='a-expander-prompt']")

# Forgot your password link
driver.find_element(By.XPATH, "//a[text()='Forgot your password?']")

# Other issues with Sign-In link
# I cannot find this link on the amazon page

# Create your Amazon account button
driver.find_element(By.ID, 'createAccountSubmit')


