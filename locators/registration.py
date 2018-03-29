"""
Locators for Login Page
"""
from selenium.webdriver.common.by import By
from locators.base import BasePageLocators


# pylint: disable=too-few-public-methods
class RegistrationPageLocators(BasePageLocators):
    """
    Locators for Login Page
    """
    FIRSTNAME_INPUT_FIELD = (By.ID, "input-firstname")
    LASTNAME_INPUT_FIELD = (By.ID, "input-lastname")
    EMAIL_INPUT_FIELD = (By.ID, "input-email")
    TELEPHONE_INPUT_FIELD = (By.ID, "input-telephone")
    PASSWORD_INPUT_FIELD = (By.ID, "input-password")
    CONFIRM_PASSWORD_INPUT_FIELD = (By.ID, "input-confirm")
    PRIVACY_POLICY_CHECKBOX = (By.NAME, "agree")
    CONTINUE_BUTTON = (By.XPATH, '//*[@id="content"]/form/div/div/input[2]')
