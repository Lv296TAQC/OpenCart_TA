"""
Cart Page comes here.
"""
from locators.cart import CartPageLocators
from .base import BasePage
from .checkout import CheckoutPage


class CartPage(BasePage):
    """
    Cart Page methods come here.
    """

    def edit_good_qty(self, qty):
        """Make webdriver change qty of product in Cart"""
        edit_field = self.driver.find_element(*CartPageLocators.QTY_FIELD)
        edit_field.clear()
        edit_field.send_keys(qty)
        self.driver.find_element(*CartPageLocators.BTN_UPDATE).click()
        return self

    def delete_good_from_cart(self):
        """Make webdriver delete product from Cart."""
        self.driver.find_element(*CartPageLocators.BTN_DELETE).click()
        self.driver.refresh()
        return self

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
        continue_button = self.driver.find_element(*CartPageLocators.BTN_CONTINUE)
        continue_button.click()
        return self
