"""
Products Page comes here.
"""
from locators.products import ProductsPageLocators
from .base import BasePage
from .product import ProductPage


# pylint: disable=too-few-public-method
class ProductsPage(BasePage):
    """
    Products Page methods come here.
    """
    def goto_mac_desctops(self):
        """Make webdriver add Mac product to Cart."""
        self.driver.find_element(*ProductsPageLocators.MAC_PRODUCT_IMAGE).click()
        return ProductPage(self.driver)
