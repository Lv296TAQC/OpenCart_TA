"""
Locators for register form are placed here
"""
from selenium.webdriver.common.by import By


# pylint: disable=too-few-public-methods
class RegisterElementLocators:
    """
    Locators for register form are placed here
    """

    FIRSTNAME = (By.ID, 'input-firstname')
    LASTNAME = (By.ID, 'input-lastname')
    EMAIL = (By.ID, 'input-email')
    TELEPHONE = (By.ID, 'input-telephone')
    PASSWORD = (By.ID, 'input - password')
    CONFIRMPASSWORD = (By.ID, 'input-confirm')
    CONTINUE = (By.XPATH, '//*[@id="content"]/form/div/div/input[2]')
    AGRI = (By.NAME, 'agree')
