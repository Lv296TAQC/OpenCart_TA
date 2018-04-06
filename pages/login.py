"""
Login Page comes here.
"""
from locators.login import LoginPageLocators
from .account import AccountPage
from .base import BasePage


class LoginPage(BasePage):
    """
    Login Page methods come here.
    """

    def input_email(self, email: str) -> object:
        """
        Make webdriver enter 'E-Mail' value.

        :param email: String with User's E-Mail address.
        :return: Login Page Object with entered E-Mail address.
        """
        self.logger.info("entering User's E-Mail")
        self.driver.find_element(*LoginPageLocators.EMAIL_INPUT_FIELD).send_keys(email)
        return self

    def input_password(self, password: str) -> object:
        """
        Make webdriver enter 'Password' value.

        :param password: String with User's password.
        :return: Login Page Object with entered password.
        """
        self.logger.info("entering User's Password")
        self.driver.find_element(*LoginPageLocators.PASSWORD_INPUT_FIELD).send_keys(password)
        return self

    def login(self) -> object:
        """
        Make webdriver initiate login by click 'Login' Button.

        :return: Account Page Object.
        """
        self.logger.info("clicking Login Button")
        self.driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
        return AccountPage(self.driver)
