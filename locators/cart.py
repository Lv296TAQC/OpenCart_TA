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
    QTY_FIELD = (By.XPATH, '//*[@id="content"]/form/div/table/tbody/tr/td[4]/div/input')
    UPDATE_BUTTON = (
        By.XPATH, '//*[@id="content"]/form/div/table/tbody/tr/td[4]/div/span/button[1]')
    DELETE_BUTTON = (
        By.XPATH, '//*[@id="content"]/form/div/table/tbody/tr/td[4]/div/span/button[2]')
