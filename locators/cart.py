"""
Locators for Cart Page are placed here
"""
from selenium.webdriver.common.by import By
from .base import BasePageLocators


# pylint: disable=too-few-public-methods
class CartPageLocators(BasePageLocators):
    """
    Locators for Cart Page are placed here
    """
    GO_CHECKOUT = (By.XPATH, '//*[@id="content"]/div[3]/div[2]/a')
    EMPTY_CART_TEXT = (By.XPATH, '//*[@id="content"]/p')
    BTN_CONTINUE = (By.XPATH, '//*[@id="content"]/div/div/a')
    QTY_FIELD = (By.XPATH, '//*[@id="content"]/form/div/table/tbody/tr/td[4]/div/input')
    BTN_UPDATE = (
        By.XPATH, '//*[@id="content"]/form/div/table/tbody/tr/td[4]/div/span/button[1]')
    BTN_DELETE = (
        By.XPATH, '//*[@id="content"]/form/div/table/tbody/tr/td[4]/div/span/button[2]')

    BTN_DELETE_PRODUCT = (By.CLASS_NAME, 'btn btn-danger')
    BTN_EDIT_QTY = (By.CLASS_NAME, 'btn-primary')
    FIELD_PRODUCT_QTY = (By.CLASS_NAME, 'form-control')

    @staticmethod
    def find_product_edit_field(edit_model: str) -> tuple:
        """
        Wrapper for product edit field locator.

        :param edit_model: Model of product, which quantity we want to edit.
        :return: Tuple for finding product's edit field
        """
        field = (By.XPATH, '//a[text()="{}"]'.format(edit_model))
        return field

    @staticmethod
    def find_product_delete_field(delete_model: str) -> tuple:
        """
        Wrapper for product delete field locator.

        :param delete_model: Model of product, which we want to delete from Cart.
        :return: Tuple for finding product's delete button
        """
        delete = (By.XPATH, '//a[text()="{}"]'.format(delete_model))
        return delete
