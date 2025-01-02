from time import sleep

from selenium.webdriver.common.by import By
from behave import given, when, then



@given('Open target main page')
def open_main(context):
    context.app.main_page.open_main()
@when('Search for {product}')
def search_product(context, product):
    context.app.header.search_product(product)

@when('Click on Cart icon')
def click_cart(context):
    context.app.header.click_cart()


@then('Verify at least 1 header link is shown')
def verify_header_links(context):
    el = context.driver.find_element(By.CSS_SELECTOR, "[data-test*='@web/GlobalHeader/UtilityHeader/']")
    print('\nFind element:')
    print(el)
    # StaleElRefException:
    # context.driver.refresh()
    # sleep(5)
    # el = context.driver.find_element(By.CSS_SELECTOR, "[data-test*='@web/GlobalHeader/UtilityHeader/']")
    # print('\nAfter REFRESH, find element:')
    # print(el)
    # el.click()
    # sleep(3)


@then('Verify {expected_amount} header links are shown')
def verify_header_links_amount(context, expected_amount):
    links = context.driver.find_elements(By.CSS_SELECTOR, "[data-test*='@web/GlobalHeader/UtilityHeader/']")
    print('\nFind elements:')
    print(links)
    print(type(len(links)))
    assert len(links) == int(expected_amount), f'Expected {expected_amount} links but got {len(links)}'

