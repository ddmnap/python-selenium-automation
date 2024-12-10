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

# Navigate to the Amazon website sign in page
driver.get("https://www.amazon.ca/ap/signin?openid.mode=checkid_setup&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&openid.return_to=https%3A%2F%2Fwww.amazon.ca%2Fref%3Drhf_sign_in&openid.assoc_handle=caflex&openid.pape.max_auth_age=0")

# Wait for the page to load
sleep(3)

# Amazon logo
driver.find_element(By.XPATH, "//i[@class='a-icon a-icon-logo' and @aria-label='Amazon']")

# Email field
driver.find_element(By.ID, 'ap_email')

# Continue button
driver.find_element(By.ID, 'continue')

# Conditions of use link
driver.find_element(By.XPATH, "//a[contains(@class, 'a-link-normal') and contains(text(), 'Conditions of Use')]")

# Privacy Notice link
driver.find_element(By.XPATH, "//a[contains(@class, 'a-link-normal') and contains(text(), 'Privacy Notice')]")

# Need help link
driver.find_element(By.XPATH, "//span[contains(@class, 'a-expander-prompt') and contains(text(), 'Need help?')]")

# I do not have Forgot your password link

# Shop on Amazon Business
driver.find_element(By.ID, 'ab-signin-ingress-link')

# I do not have Other issues with Sign-In link

# Create your Amazon account button
driver.find_element(By.ID, 'createAccountSubmit')
