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

#Clicking on orders button
driver.find_element(By.ID, 'nav-orders').click()

#Confirming Sign In header is visible and email input field is present
driver.find_element(By.XPATH, "//h1[@class='a-spacing-small']")
driver.find_element(By.ID, 'ap_email')

expected_text = 'Sign in'
actual_text = driver.find_element(By.XPATH, "//h1[@class='a-spacing-small']").text

assert actual_text == expected_text, f'Expected {expected_text} but got {actual_text}'

# Verify email field present
driver.find_element(By.ID, 'ap_email')

print('Test Passed')

sleep(15)
driver.quit()


