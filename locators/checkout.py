"""
Checkout Page locators come here
"""
from selenium.webdriver.common.by import By
from .base import BasePageLocators


# pylint: disable=too-few-public-methods
class CheckoutPageLocators(BasePageLocators):
    """
    It contents constants
    """
    ACCORDION = (By.ID, 'accrodion')

    GUEST_ACCOUNT = (By.CSS_SELECTOR, '[type="radio"][name="account"][value="guest"]')
    REGISTER_ACCOUNT = (By.CSS_SELECTOR, '[type="radio"][name="account"][value="register"]')

    BTN_ACCOUNT = (By.ID, 'button-account')
    BTN_LOGIN = (By.ID, 'button-login')
    BTN_GUEST = (By.ID, 'button-guest')

    FIRST_NAME = (By.ID, 'input-payment-firstname')
    LAST_NAME = (By.ID, 'input-payment-lastname')
    EMAIL = (By.ID, 'input-payment-email')
    TELEPHONE = (By.ID, 'input-payment-telephone')
    FAX = (By.ID, 'input-payment-fax')

    COMPANY = (By.ID, 'input-payment-company')
    ADDRESS_1 = (By.ID, 'input-payment-address-1')
    ADDRESS_2 = (By.ID, 'input-payment-address-2')
    CITY = (By.ID, 'input-payment-city')
    POST_CODE = (By.ID, 'input-payment-postcode')
    COUNTRY = (By.ID, 'input-payment-country')
    REGION_OR_STATE = (By.ID, 'input-payment-zone')
