"""
Contains EditAccountLocators class with EditAccount page element locators.
"""
from selenium.webdriver.common.by import By
from .base import BasePageLocators


# pylint: disable=too-few-public-methods
class EditAccountLocators(BasePageLocators):
    """
    Contains constants with EditAccount page element locators.
    """

    FIRSTNAME_FIELD = (By.ID, "input-firstname")
    LASTNAME_FIELD = (By.ID, "input-lastname")
    EMAIL_FIELD = (By.ID, "input-email")
    TELEPHONE_FIELD = (By.ID, "input-telephone")
    BTN_CONTINUE = (By.XPATH, "//form[@class='form-horizontal']/div/div[2]/input")
    FIRSTNAME_ERROR = (By.XPATH, "//form[@class='form-horizontal']/fieldset/div[1]/div/div")
    LASTNAME_ERROR = (By.XPATH, "//form[@class='form-horizontal']/fieldset/div[2]/div/div")
    TELEPHONE_ERROR = (By.XPATH, "//form[@class='form-horizontal']/fieldset/div[4]/div/div")
