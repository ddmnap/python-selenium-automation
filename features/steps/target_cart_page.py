from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# Set up Selenium
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# Step Definitions

@given('I open the Target main page')
def open_main_page(context):
    context.driver = driver
    context.driver.get('https://www.target.com/')
    WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '.sc-e487bf3b-1.iZzjLF'))
    )

@when('Search for mug')
def search_for_mug(context):
    search_box = context.driver.find_element(By.ID, "search")
    search_box.send_keys("mug")
    search_box.send_keys(Keys.RETURN)
    WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'Add to cart')]"))
    )

@when('Click on Add to Cart button')
def click_add_to_cart(context):
    add_to_cart_button = context.driver.find_element(By.XPATH, "(//button[contains(text(), 'Add to cart')])[1]")
    add_to_cart_button.click()
    WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'View cart & check out')]"))
    )

@when('Confirm Add to Cart button from side navigation')
def confirm_add_to_cart(context):
    confirm_button = context.driver.find_element(By.XPATH, "//button[contains(text(), 'View cart & check out')]")
    confirm_button.click()
    WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//a[@aria-label='Cart']"))
    )

@when('Open cart page')
def open_cart_page(context):
    cart_icon = context.driver.find_element(By.XPATH, "//a[@aria-label='Cart']")
    cart_icon.click()
    WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[contains(text(), '1 item')]"))
    )

@then('I should see cart has 1 item(s)')
def verify_cart_item_count(context):
    cart_count = context.driver.find_element(By.XPATH, "//span[contains(text(), '1 item')]")
    assert "1 item" in cart_count.text, "Cart does not contain 1 item."
    context.driver.quit()
