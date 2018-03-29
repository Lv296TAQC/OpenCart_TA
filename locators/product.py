"""
Locators for Product Page
"""
from selenium.webdriver.common.by import By
from locators.base import BasePageLocators


# pylint: disable=too-few-public-methods
class ProductPageLocators(BasePageLocators):
    """
    Locators for Product Page
    """
    BTN_CART = (By.ID, 'button-cart')
    ADD_APPLE_CINEMA = (By.XPATH, '//*[@id="content"]/div[3]/div[1]/div/div[2]/div[2]/button[1]')
    GO_TO_IMAC = (By.XPATH, '//*[@id="content"]/div[2]/div/div/div[1]/a/img')
    ADD_IMAC_TO_CART = (By.ID, "button-cart")
