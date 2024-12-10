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


@given("I open the Target website")
def open_target_website(context):
    driver.get("https://www.target.com/")


@when("I click on the Sign In button")
def click_sign_in_button(context):
    sign_in = driver.find_element(By.CSS_SELECTOR, '.sc-58ad44c0-3.kkWqdY.h-margin-r-x3')
    sign_in.click()


@when("I click on the Sign In from the side menu")
def click_side_menu_sign_in(context):
    side_sign_in = driver.find_element(By.CSS_SELECTOR, '.sc-ddc722c0-0.sc-f1230b39-0.flfJAZ.jtKdbk.h-margin-t-x2.h-margin-b-default')
    side_sign_in.click()
    sleep(3)  # Wait for the page to load


@then("I should see the Sign In form")
def verify_sign_in_form(context):
    sign_in_form = driver.find_element(By.CSS_SELECTOR, '.sc-fe064f5c-0.sc-315b8ab9-2.lnvRvp.diHlfH')
    assert sign_in_form is not None, "Sign In form is not displayed."

    # Close the browser at the end of the test
    driver.quit()
