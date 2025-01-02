from pages.base_page import BasePage


class MainPage(BasePage):

    def open_main(self):
        self.open_url('https://www.target.com/')

    def click_sign_in(self):
        self.driver.find_element(*self.SIGN_IN_BUTTON).click()