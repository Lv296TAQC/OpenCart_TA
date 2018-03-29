from models.basepage import BasePage
from models.locators import CartPageLocators


class CartPage(BasePage):

    def go_to_checkout(self):
        element = self.driver.find_element(*CartPageLocators.GO_CHECKOUT)
        element.click()
