from models.basepage import BasePage
from models.locators import ProductPageLocators


class ProductPage(BasePage):

    def add_to_cart(self):
        element = self.driver.find_element(*ProductPageLocators.BTN_CART)
        element.click()

    def go_to_cart(self):
        element = self.driver.find_element(*ProductPageLocators.GO_CART)
        element.click()
