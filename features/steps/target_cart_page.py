from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# Set up Selenium
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.maximize_window()

@given('I open the Target main page')
def open_main_page(context):
    driver.get('https://www.target.com/')
    sleep(10)  # Allow the page to load

@when('I click on the Cart icon')
def click_cart_icon(context):
    cart_icon = driver.find_element(By.CSS_SELECTOR, '.sc-e487bf3b-1.iZzjLF')
    cart_icon.click()
    sleep(10)  # Allow the Cart page to load

@then('I should see "Your cart is empty" message')
def verify_cart_message(context):
    empty_cart_message = driver.find_element(By.CSS_SELECTOR, '.sc-fe064f5c-0.fJliSz')
    assert "Your cart is empty" in empty_cart_message.text, "Cart message is incorrect."

    # Close the browser at the end of the test
    driver.quit()