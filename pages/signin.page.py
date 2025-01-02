from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class SignInPage(BasePage):
    SIGN_IN_FORM = (By.CSS_SELECTOR, '.sc-fe064f5c-0.sc-315b8ab9-2.lnvRvp.diHlfH')

    def is_sign_in_form_displayed(self):
        return self.driver.find_element(*self.SIGN_IN_FORM).is_displayed()
