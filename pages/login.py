"""
Login Page Object Model
"""
from locators.login import LoginPageLocators
from pages.base import BasePage


class LoginPage(BasePage):
    """
    Login Page Object Model
    """
    def input_email(self):
        """Make webdriver set 'E-Mail' value."""
        input_email = self.driver.find_element(*LoginPageLocators.EMAIL_INPUT_FIELD)
        input_email.send_keys('oleksandr.makar.ol@gmail.com')
        return self

    def input_password(self):
        """Make webdriver set 'Password' value."""
        input_password = self.driver.find_element(*LoginPageLocators.PASSWORD_INPUT_FIELD)
        input_password.send_keys('saxon123')
        return self

    def login(self):
        """Make webdriver initiate login by click 'Login' Button"""
        login = self.driver.find_element(*LoginPageLocators.LOGIN_BUTTON)
        login.click()
        return self
