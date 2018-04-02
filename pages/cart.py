"""
Cart Page Object Model
"""
from pages.base import BasePage
from locators.cart import CartPageLocators


class CartPage(BasePage):
    """
    Cart Page Object Model
    """
    def edit_good_qty(self):
        """Make webdriver change qty of product in Cart"""
        edit_good_qty = self.driver.find_element(*CartPageLocators.GOOD_QTY_FIELD)
        edit_good_qty.clear()
        edit_good_qty.send_keys('2')
        update_good_qty = self.driver.find_element(*CartPageLocators.UPDATE_GOOD_QTY_BUTTON)
        update_good_qty.click()
        return self

    def delete_good_from_cart(self):
        """Make webdriver delete product from Cart."""
        delete_good = self.driver.find_element(*CartPageLocators.DELETE_GOOD_BUTTON)
        delete_good.click()
        return self

    def go_to_checkout(self):
        """
        TODO
        """
        element = self.driver.find_element(*CartPageLocators.GO_CHECKOUT)
        element.click()
        return self

    def is_on_cart_page(self):
        """
        TODO
        """
        if self.driver.current_url == "http://127.0.0.1/opencart.com/index.php?route=checkout/cart":
            print(True)
            return True
        print(False)
        return False

    def is_cart_empty(self):
        """
        TODO
        """
        empty_cart_text = self.driver.find_element(*CartPageLocators.EMPTY_CART_TEXT)
        if empty_cart_text:
            print("Yout cart is empty!")
            return True
        return False

    def click_on_continue_button(self):
        """
        TODO
        """
        continue_button = self.driver.find_element(*CartPageLocators.CONTINUE_BUTTON)
        continue_button.click()
        return self
