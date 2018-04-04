"""
TODO
"""
from pages.base import BasePage
from locators.product import ProductPageLocators
from pages.cart import CartPage


class ProductPage(BasePage):
    """
    TODO
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
