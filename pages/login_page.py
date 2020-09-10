from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, f"No \'login\' substring in current URL: {self.browser.current_url}"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_USERNAME), "Login username edit is not presented"
        assert self.is_element_present(*LoginPageLocators.LOGIN_PASSWORD), "Login password is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_USERNAME), "Register username is not presented"
        assert self.is_element_present(*LoginPageLocators.LOGIN_PASSWORD), "Register password is not presented"
        assert self.is_element_present(*LoginPageLocators.LOGIN_PASSWORD), "Register confirm password is not presented"
