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
driver.get("https://www.amazon.ca/ap/register?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.ca%2Fref%3Drhf_sign_in&prevRID=CG3NCRBPVPZKX3EQ655P&openid.assoc_handle=caflex&openid.mode=checkid_setup&prepopulatedLoginId=&failedSignInCount=0&pageId=caflex&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0")

# Wait for the page to load
sleep(3)

element = driver.find_element(By.CSS_SELECTOR, '.a-icon.a-icon-logo')
element_1 = driver.find_element(By.CSS_SELECTOR, '.a-spacing-small')
element_2 = driver.find_element(By.CSS_SELECTOR, '#ap_customer_name')
element_3 = driver.find_element(By.CSS_SELECTOR, '#ap_email')
element_4 = driver.find_element(By.CSS_SELECTOR, '#ap_password')
element_5 = driver.find_element(By.CSS_SELECTOR, '.a-alert-content')
element_6 = driver.find_element(By.CSS_SELECTOR, '#ap_password_check')
element_7 = driver.find_element(By.CSS_SELECTOR, '#continue')
element_8 = driver.find_element(By.CSS_SELECTOR, 'a[href*="condition_of_use"]')
element_9 = driver.find_element(By.CSS_SELECTOR, 'a[href*="privacy_notice"]')
element_10 = driver.find_element(By.CSS_SELECTOR, '.a-link-emphasis')









