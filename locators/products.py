"""
TODO
"""
from selenium.webdriver.common.by import By
from .base import BasePageLocators


# pylint: disable=too-few-public-methods
class ProductsPageLocators(BasePageLocators):
    """
    TODO
    """
    MAC_PRODUCT_IMAGE = (By.XPATH, '//*[@id="content"]/div[2]/div/div/div[1]/a/img')
    BTN_CART = (By.ID, 'button-cart')
