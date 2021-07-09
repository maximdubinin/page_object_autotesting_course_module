import time

from .base_page import BasePage
from .locators import LoginPageLocators
from .locators import BasePageLocators


class LoginPage(BasePage):
    def register_new_user(self, email, password):
        self.should_be_login_page()
        email_input = self.browser.find_element(*LoginPageLocators.EMAIL_INPUT)
        email_input.send_keys(email)
        password_input = self.browser.find_element(*LoginPageLocators.PASSWORD_INPUT)
        password_input.send_keys(password)
        password_confirmation_input = self.browser.find_element(*LoginPageLocators.PASSWORD_CONFIRMATION_INPUT)
        password_confirmation_input.send_keys(password)
        register_submit = self.browser.find_element(*LoginPageLocators.REGISTER_SUBMIT)
        register_submit.click()
        self.should_be_register_success_message()
        self.should_be_logged_in_user()

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert self.url.find(LoginPageLocators.LOGIN_URL_IDENTIFIER),\
            f"Opened page URL is not login page URL, actually '{self.url})'"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form was not found, but should be"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form was not found, but should be"

    def should_be_register_success_message(self):
        assert self.is_element_present(*BasePageLocators.SUCCESS_MESSAGE), \
            "Register success_message is not present, but should be"

    def should_be_logged_in_user(self):
        assert self.is_element_present(*BasePageLocators.USER_ICON), "User is not logged in, but should be"
