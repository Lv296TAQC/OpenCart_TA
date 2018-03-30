"""
TODO
"""
from pages.base import BasePage
from locators.cart import CartPageLocators


class CartPage(BasePage):
    """
    TODO
    """

    def edit_good_qty(self):
        """Make webdriver change qty of product in Cart"""
        self.driver.find_element_by_xpath(
            '//*[@id="content"]/form/div/table/tbody/tr/td[4]/div/input').clear()
        self.driver.find_element_by_xpath(
            '//*[@id="content"]/form/div/table/tbody/tr/td[4]/div/input').send_keys('2')
        self.driver.find_element_by_xpath(
            '//*[@id="content"]/form/div/table/tbody/tr/td[4]/div/span/button[1]').click()

    def delete_good_from_cart(self):
        """Make webdriver delete product from Cart."""
        self.driver.find_element_by_xpath(
            '//*[@id="content"]/form/div/table/tbody/tr/td[4]/div/span/button[2]').click()

    def go_to_checkout(self):
        """
        TODO
        """
        element = self.driver.find_element(*CartPageLocators.GO_CHECKOUT)
        element.click()

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
