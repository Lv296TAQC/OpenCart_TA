"""
Account Page comes here.
"""
from .base import BasePage
from locators.account import AccountLocators


class AccountPage(BasePage):
    """
    Account Page methods come here.
    """
    def open_address_book_page(self):
        """
        TODO
        """
        self.driver.find_element(*AccountLocators.ADDRESS_BOOK_LINK)
        return self

    def open_user_edit_page(self):
        """
        TODO
        """
        self.driver.find_element(*AccountLocators.EDIT_ACCOUNT_LINK)
        return self
