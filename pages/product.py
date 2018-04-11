"""
Product Page comes here.
"""
import logging

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from locators.product import ProductPageLocators
from .base import BasePage
from .cart import CartPage


# pylint: disable=too-few-public-methods
class ProductPage(BasePage):
    """
    Product Page methods come here.
    """

    def add_to_cart(self) -> "ProductPage":
        """
        Make webdriver add product to Cart.

        :return: Product Page Object with added product into Cart.
        """
        logging.info('adding product to the Cart')
        self.driver.find_element(*ProductPageLocators.BTN_CART).click()
        self.driver.implicitly_wait(5)
        return self

    def goto_cart(self) -> object:
        """
        Make webdriver go to Cart Page.

        :return: Cart Page Object.
        """
        logging.info('clicking Cart Link in top Bar')
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(ProductPageLocators.GO_CART)
        )
        self.driver.find_element(*ProductPageLocators.GO_CART).click()
        return CartPage(self.driver)
