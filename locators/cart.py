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
    EMPTY_CART_TEXT = (By.XPATH, '//p[text()="Your shopping cart is empty!"]')
    BTN_CONTINUE = (By.XPATH, '//*[@id="content"]/div/div/a')
    QTY_FIELD = (By.XPATH, '//*[@id="content"]/form/div/table/tbody/tr/td[4]/div/input')
    BTN_UPDATE = (
        By.XPATH, '//*[@id="content"]/form/div/table/tbody/tr/td[4]/div/span/button[1]')
    BTN_DELETE = (
        By.XPATH, '//*[@id="content"]/form/div/table/tbody/tr/td[4]/div/span/button[2]')

    BTN_DELETE_PRODUCT = (By.CLASS_NAME, 'btn btn-danger')
    BTN_EDIT_QTY = (By.CLASS_NAME, 'btn-primary')
    FIELD_PRODUCT_QTY = (By.CLASS_NAME, 'form-control')
    MODIFIED_CART_TEXT = (
        By.XPATH, '//div[contains(text(),"You have modified your shopping cart!")]')
    TOTAL_SUM = (By.XPATH, '//*[@id="content"]/form/div/table/tbody/tr/td[6]')
    ALERT_TOO_MUCH_PRODUCT = (By.XPATH, '//*[@id="checkout-cart"]/div[2]')
    PRODUCT_ROW = (By.XPATH, "//button[2]")
    QTY_FIELD = (By.TAG_NAME, "input")

    @staticmethod
    def product_number(number: int) -> tuple:
        """
        Wrapper for product locator on the Cart page.

        :param number: Name of product need to be added
        :return: WebElement locator
        """
        product_row = (By.XPATH, '//*[@id="content"]/form/div/table/tbody/tr[{}]'.format(number))
        return product_row

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

    @staticmethod
    def find_product_link(product_name: str) -> tuple:
        """
        Wrapper for product name locator on the Cart page.

        :param product_name: Name of product need to be added
        :return: WebElement locator
        """
        link = (By.XPATH, '//td[2]/a[text()="{}"]'.format(product_name))
        return link
