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

driver.get('https://www.target.com/')

# Click SignIn button
driver.find_element(By.XPATH, "//span[text()='Sign in']").click()



# Click SignIn from side navigation
driver.find_element(By.XPATH, "//a[@data-test='accountNav-signIn']").click()

sleep(4)

# Verify SignIn page opened:
expected_text = 'Sign into your Target account'
actual_text = driver.find_element(By.XPATH, "//span[text()='Sign into your Target account']")

print("Test case passed")

driver.quit()

