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

@given("I open the Target Circle page")
def open_target_circle_page(context):
    driver.get("https://www.target.com/l/target-circle/-/N-pzno9")
    sleep(3)  # Wait for the page to load

@when("I count the number of benefit cells")
def count_benefit_cells(context):
    context.elements = driver.find_elements(By.CSS_SELECTOR, ".filmstrip-with-storyblocks-ie-11-fix")
    context.count = len(context.elements)  # Count the number of elements found

@then("I should find at least 10 benefit cells")
def verify_benefit_cells(context):
    assert context.count >= 10, f"Expected at least 10 benefit cells, but found {context.count}."
    print(f"Number of benefit cells found: {context.count}")
    driver.quit()
