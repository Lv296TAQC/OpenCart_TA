"""
Contains the PasswordPage class for interacting with the Password page.
"""
import hashlib
import logging
from locators.password import PasswordLocators
from models.password import Password
from .base import BasePage


# pylint: disable=too-few-public-methods
class PasswordPage(BasePage):
    """
    Contains methods for interacting with the Password page.
    """

    @staticmethod
    def encrypt_user_password(password: Password, salt: Password, encoding='utf-8') -> Password:
        """
        Provide user's password encryption.

        :param password: user's password.
        :param salt: salt data from db table oc_customer.
        :param encoding: utf-8 encoding.
        :return: Password object with hash data.
        """
        logging.info(f"Convert password: {password} and salt: {salt} into hashed password.")
        step1 = hashlib.sha1(password.password.encode(encoding))
        step2 = hashlib.sha1(salt.salt.encode(encoding) + step1.hexdigest().encode(encoding))
        step3 = hashlib.sha1(salt.salt.encode(encoding) + step2.hexdigest().encode(encoding))
        return Password(password=step3.hexdigest())

    @staticmethod
    def _change_password_in_text_fields(form_textfield: "WebElement", data: Password):
        """
        Enter the data in the textfield.

        :param form_textfield: textfield's id.
        :param data: data entered in the textfield.
        """
        logging.info(f"Set {data} into {form_textfield} text field.")
        if data is not None:
            form_textfield.click()
            form_textfield.clear()
            form_textfield.send_keys(data)

    def fill_password_form(self, user_data: Password) -> "PasswordPage":
        """
        Change user data in the Edit Account form.

        :param user_data: data entered in the textfield.
        :return: PasswordPage object.
        """
        self._change_password_in_text_fields(
            self.driver.find_element(*PasswordLocators.PASSWORD_FIELD), user_data.password)
        self._change_password_in_text_fields(
            self.driver.find_element(*PasswordLocators.PASSWORD_CONFIRM_FIELD), user_data.password)
        self.driver.find_element(*PasswordLocators.BTN_CONTINUE).click()
        return self
