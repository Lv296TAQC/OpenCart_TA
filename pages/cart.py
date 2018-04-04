"""
TODO
"""
# pylint: disable=cyclic-import
from locators.cart import CartPageLocators
from pages.base import BasePage
from pages.checkout import CheckoutPage
from pages.home import HomePage


class CartPage(BasePage):
    """
    TODO
    """

    def edit_good_qty(self, qty):
        """Make webdriver change qty of product in Cart"""
        edit_field = self.driver.find_element(*CartPageLocators.QTY_FIELD).clear()
        edit_field.send_keys(qty)
        self.driver.find_element(*CartPageLocators.UPDATE_BUTTON).click()
        return self

    def delete_good_from_cart(self):
        """Make webdriver delete product from Cart."""
        self.driver.find_element_by_xpath(
            '//*[@id="content"]/form/div/table/tbody/tr/td[4]/div/span/button[2]').click()

    def goto_checkout(self):
        """
        TODO
        """
        element = self.driver.find_element(*CartPageLocators.GO_CHECKOUT)
        element.click()
        return CheckoutPage(self.driver)

    def is_on_cart_page(self):
        """
        TODO
        """
        if self.driver.current_url == "https://demo.opencart.com/index.php?route=checkout/cart":
            return True
        return False

    def is_cart_empty(self):
        """
        TODO
        """
        empty_cart_text = self.driver.find_element(*CartPageLocators.EMPTY_CART_TEXT)
        if empty_cart_text:
            return True
        return False

    def click_on_continue_button(self):
        """
        TODO
        """
        continue_button = self.driver.find_element(*CartPageLocators.CONTINUE_BUTTON)
        continue_button.click()
        return HomePage(self.driver)
