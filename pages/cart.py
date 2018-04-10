"""
Cart Page comes here.
"""
import logging

from urllib.parse import urlparse
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from locators.cart import CartPageLocators
from locators.products import ProductsPageLocators
from .base import BasePage
from .checkout import CheckoutPage


class CartPage(BasePage):
    """
    Cart Page methods come here.
    """

    def edit_good_qty(self, qty: int) -> object:
        """
        Make webdriver change qty of first product in Cart.

        :param qty: Quantity of product, that you want to get after update.
        :return: Cart Page Object with changed qty of first product in Cart.
        """
        logging.info('editing first product quantity in Cart')
        edit_field = self.driver.find_element(*CartPageLocators.QTY_FIELD)
        edit_field.clear()
        edit_field.send_keys(qty)
        self.driver.find_element(*CartPageLocators.BTN_UPDATE).click()
        return self

    def delete_good_from_cart(self) -> "CartPage":
        """
        Make webdriver delete first product from Cart.
        Refresh browser page for make shore changes will appear.

        :return: Cart Page Object with deleted first product in Cart.
        """
        logging.info('deleting first product from Cart')
        self.driver.find_element(*CartPageLocators.BTN_DELETE).click()
        self.driver.refresh()
        return self

    def edit_product_qty_by_model(self, edit_model: str, qty: int) -> "CartPage":
        """
        Make webdriver edit quantity of certain product to Cart

        :param edit_model: Model of product, which quantity we want to edit.
        :param qty: Quantity of product, that you want to get after update.
        :return: Cart Page Object with edited certain product quantity.
        """
        logging.info('editing quantity of certain product in Cart by model')
        if edit_model == "Product 11":
            edit_model = edit_model.lower()
        edit_field = self.driver.find_element(
            *CartPageLocators.find_product_edit_field(edit_model))
        edit_field.clear()
        edit_field.send_keys(qty)
        edit_field.send_keys(Keys.ENTER)
        return self

    def delete_product_by_model(self, delete_model: str) -> "CartPage":
        """
        Make webdriver delete certain product from Cart

        :param delete_model: Model of product, which we want to delete from cart.
        :return: Cart Page Object with deleted certain product from cart.
        """
        logging.info('editing quantity of certain product in Cart by model')
        if delete_model == "Product 11":
            delete_model = delete_model.lower()
        self.driver.find_element(
            *CartPageLocators.find_product_delete_field(delete_model)).click()
        self.driver.refresh()
        return self

    def goto_checkout(self):
        """
        TODO
        """
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(CartPageLocators.GO_CHECKOUT)
        )
        element = self.driver.find_element(*CartPageLocators.GO_CHECKOUT)
        element.click()
        return CheckoutPage(self.driver)

    def is_on_cart_page(self):
        """
        TODO
        """
        current_url_path = urlparse(self.driver.current_url).path
        if current_url_path == "/opencart.com/index.php?route=checkout/cart":
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

    def is_product_added(self, product_name):
        """
        TODO
        """
        if self.driver.find_element(*ProductsPageLocators.find_product_link(product_name)):
            return True
        return False

    def click_on_continue_button(self):
        """
        TODO
        """
        self.driver.find_element(*CartPageLocators.BTN_CONTINUE).click()
        return self.driver

    def edit_product_qty(self, qty):
        """
        TODO
        """
        field_edit = self.driver.find_elements(*CartPageLocators.FIELD_PRODUCT_QTY)
        field_edit[1].clear()
        field_edit[1].send_keys(qty)
        btn_edit = self.driver.find_elements(*CartPageLocators.BTN_EDIT_QTY)
        btn_edit[0].click()
        return self

    def delete_product_from_cart(self):
        """
        TODO
        """
        delete_buttons = self.driver.find_elements(*CartPageLocators.BTN_DELETE_PRODUCT)
        delete_buttons[0].click()
        return self
