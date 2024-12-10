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
sign_in_button=driver.find_element(By.XPATH, "//span[contains(@class, 'sc-58ad44c0-3 kwbrXj h-margin-r-x3') and contains(text(), 'Sign in')]")

sign_in_button.click()

# Click SignIn from side navigation
sign_in_button_side_navigation=driver.find_element(By.XPATH, "//button[contains(@class, 'sc-ddc722c0-0 sc-f1230b39-0 jKTcnK doBYzz h-margin-t-x2 h-margin-b-default') and contains(text(), 'Sign in')]")

sign_in_button_side_navigation.click()

# Wait for the page to load
sleep(3)

# Verify SignIn page opened
driver.find_element(By.XPATH, "//span[text()='Sign into your Target account']")

