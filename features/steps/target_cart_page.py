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


class Keys:
    pass


@then('I should see "Your cart is empty" message')
def verify_cart_message(context):
    empty_cart_message = driver.find_element(By.CSS_SELECTOR, '.sc-fe064f5c-0.fJliSz')
    assert "Your cart is empty" in empty_cart_message.text, "Cart message is incorrect."

    # Close the browser at the end of the test
    driver.quit()


@given("I open the Target main page")
def open_target_main_page(context):
        driver.get("https://www.target.com/")
        sleep(5)  # Allow the page to load

@when("Search for mug")
def search_for_mug(context):
        search_box = driver.find_element(By.ID, "search")
        search_box.send_keys("mug")
        search_box.send_keys(Keys.RETURN)
        sleep(5)  # Wait for search results to load

@when("Click on Add to Cart button")
def click_add_to_cart(context):
        add_to_cart_button = driver.find_element(By.XPATH, "(//button[contains(text(), 'Add to cart')])[1]")
        add_to_cart_button.click()
        sleep(3)  # Allow the side navigation to open

@when("Confirm Add to Cart button from side navigation")
def confirm_add_to_cart(context):
        confirm_button = driver.find_element(By.XPATH, "//button[contains(text(), 'View cart & check out')]")
        confirm_button.click()
        sleep(3)  # Allow the cart page to load

@when("Open cart page")
def open_cart_page(context):
        cart_icon = driver.find_element(By.XPATH, "//a[@aria-label='Cart']")
        cart_icon.click()
        sleep(3)  # Wait for the cart page to load

@then("I should see cart has 1 item(s)")
def verify_cart_item_count(context):
        cart_count = driver.find_element(By.XPATH, "//span[contains(text(), '1 item')]")
        assert "1 item" in cart_count.text, "Cart does not contain 1 item"
        driver.quit()
