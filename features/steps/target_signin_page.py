from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

from behave import given, when, then

@given("I open the Target website")
def open_target_website(context):
    context.app.main_page.open_main()

@when("I click on the Sign In button")
def click_sign_in_button(context):
    context.app.main_page.click_sign_in()

@when("I click on the Sign In from the side menu")
def click_side_menu_sign_in(context):
    context.app.header_menu.click_side_sign_in()

@then("I should see the Sign In form")
def verify_sign_in_form(context):
    assert context.app.sign_in_page.is_sign_in_form_displayed(), "Sign In form is not displayed."
