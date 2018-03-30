"""
TODO
"""
from pages.base import BasePage
from locators.product import ProductPageLocators


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

    def go_to_cart(self):
        """
        TODO
        """
        element = self.driver.find_element(*ProductPageLocators.GO_CART)
        element.click()

    def add_to_cart_apple_cinema(self):
        """
        TODO
        """
        add_to_cart_button = self.driver.find_element(*ProductPageLocators.ADD_APPLE_CINEMA)
        add_to_cart_button.click()
