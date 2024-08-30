from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert "login" in self.browser.current_url.split("/"), "substring login not found in url"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "login form not found"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_FORM), "registration form not found"

    def register_new_user(self, email, password):
        email_form = self.browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL_FORM).send_keys(email)
        password_form = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD_FORM).send_keys(password)
        confirm_password = self.browser.find_element(*LoginPageLocators.REGISTRATION_CONFIRM_PASSWORD_FORM).send_keys(password)
        register_button = self.browser.find_element(*LoginPageLocators.REGISTRATION_BUTTON).click()
