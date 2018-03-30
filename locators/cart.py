"""
TODO
"""
from selenium.webdriver.common.by import By
from locators.base import BasePageLocators

# pylint: disable=too-few-public-methods
class CartPageLocators(BasePageLocators):
    """
    TODO
    """
    GO_CHECKOUT = (By.XPATH, '//*[@id="content"]/div[3]/div[2]/a')
    EMPTY_CART_TEXT = (By.XPATH, '//*[@id="content"]/p')
    CONTINUE_BUTTON = (By.XPATH, '//*[@id="content"]/div/div/a')
