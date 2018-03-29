"""
Object Model for Product Page
"""
from pages.base import BasePage
from locators.product import ProductPageLocators


class ProductPage(BasePage):
    """
    Object Model for Product Page
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
        return self

    def add_to_cart_apple_cinema(self):
        """
        TODO
        """
        add_to_cart_button = self.driver.find_element(*ProductPageLocators.ADD_APPLE_CINEMA)
        add_to_cart_button.click()
        return self

    def add_mac_to_cart(self):
        """Make webdriver add Mac product to Cart."""
        get_to_imac = self.driver.find(*ProductPageLocators.GO_TO_IMAC)
        get_to_imac.click()
        add_mac_to_cart = self.driver.find_element(*ProductPageLocators.ADD_IMAC_TO_CART)
        add_mac_to_cart.click()
        return self
