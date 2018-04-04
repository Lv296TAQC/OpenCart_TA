"""
Product Page comes here.
"""
from locators.product import ProductPageLocators
from .base import BasePage
from .cart import CartPage


class ProductPage(BasePage):
    """
    Product Page methods come here.
    """

    def add_to_cart(self):
        """
        TODO
        """
        element = self.driver.find_element(*ProductPageLocators.BTN_CART)
        element.click()
        return self

    def go_to_cart(self):
        """
        TODO
        """
        element = self.driver.find_element(*ProductPageLocators.GO_CART)
        element.click()
        return CartPage(self.driver)
