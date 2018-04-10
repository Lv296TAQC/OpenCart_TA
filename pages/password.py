"""
Contains the PasswordPage class for interacting with the Password page.
"""
import hashlib
from models.password import Password
from .base import BasePage


# pylint: disable=too-few-public-methods
class PasswordPage(BasePage):
    """
    Contains methods for interacting with the Password page.
    """

    @staticmethod
    def encrypt_customer_password(password: str, salt: str) -> Password:
        """
        Provide user's password encryption.

        :param password: user's password.
        :param salt: salt data from db table oc_customer.
        :return: Password object with hash data.
        """
        encoded_password = password.encode('utf-8')
        encoded_salt = salt.encode('utf-8')
        step1 = hashlib.sha1()
        step1.update(encoded_password)
        step2 = hashlib.sha1()
        step2.update(encoded_salt + step1.hexdigest().encode('utf-8'))
        step3 = hashlib.sha1()
        step3.update(encoded_salt + step2.hexdigest().encode('utf-8'))
        step4 = step3.hexdigest()
        return Password(password=step4)
