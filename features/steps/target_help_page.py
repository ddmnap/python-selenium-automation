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

@given("I open the Target Help page")
def open_target_help_page(context):
    driver.get("https://help.target.com/help")
    sleep(3)  # Wait for the page to load


@when("I locate the page elements")
def locate_elements(context):
    context.element = driver.find_element(By.CSS_SELECTOR, '.custom-h2')
    context.element_2 = driver.find_element(By.CSS_SELECTOR, '#j_id0:j_id2:j_id32:name')
    context.element_3 = driver.find_element(By.CSS_SELECTOR, '.btn-sm.search-btn')
    context.element_4 = driver.find_elements(By.CSS_SELECTOR, '.boxSmall.txtAC')
    context.element_5 = driver.find_elements(By.CSS_SELECTOR, '.col-lg-12')
    context.element_6 = driver.find_elements(By.CSS_SELECTOR, '.grid_4.boxSmallr.txtAC.bigbox2')
    context.element_7 = driver.find_element(By.CSS_SELECTOR, '#divID1')


@then("I close the browser")
def close_browser(context):
    driver.quit()




