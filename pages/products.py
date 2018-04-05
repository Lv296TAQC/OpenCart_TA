"""
TODO
"""
from .base import BasePage


# pylint: disable=too-few-public-methods
class ProductsPage(BasePage):
    """
    TODO
    """
    def add_mac_to_cart(self):
        """Make webdriver add Mac product to Cart."""
        self.driver.find_element_by_xpath('//*[@id="content"]/div[2]/div/div/div[1]/a/img').click()
        self.driver.find_element_by_id("button-cart").click()
