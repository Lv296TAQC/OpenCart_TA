"""
Locators for Checkout Page are placed here
"""
from selenium.webdriver.common.by import By
from .base import BasePageLocators


# pylint: disable=too-few-public-methods
class CheckoutPageLocators(BasePageLocators):
    """
    Locators for Checkout Page are placed here
    """
    ACCORDION = (By.ID, 'accrodion')

    GUEST_ACCOUNT = (By.CSS_SELECTOR, '[type="radio"][name="account"][value="guest"]')
    REGISTER_ACCOUNT = (By.CSS_SELECTOR, '[type="radio"][name="account"][value="register"]')

    BTN_ACCOUNT = (By.ID, 'button-account')
    BTN_LOGIN = (By.ID, 'button-login')
    BTN_GUEST = (By.ID, 'button-guest')

    FIRST_NAME_PAYMENT = (By.ID, 'input-payment-firstname')
    LAST_NAME_PAYMENT = (By.ID, 'input-payment-lastname')
    EMAIL_PAYMENT = (By.ID, 'input-payment-email')
    TELEPHONE_PAYMENT = (By.ID, 'input-payment-telephone')
    FAX_PAYMENT = (By.ID, 'input-payment-fax')

    COMPANY_PAYMENT = (By.ID, 'input-payment-company')
    ADDRESS_1_PAYMENT = (By.ID, 'input-payment-address-1')
    ADDRESS_2_PAYMENT = (By.ID, 'input-payment-address-2')
    CITY_PAYMENT = (By.ID, 'input-payment-city')
    POST_CODE_PAYMENT = (By.ID, 'input-payment-postcode')
    COUNTRY_PAYMENT = (By.ID, 'input-payment-country')
    REGION_OR_STATE_PAYMENT = (By.ID, 'input-payment-zone')

    E_MAIL = (By.ID, 'input-email')
    PASSWORD = (By.ID, 'input-password')

    RADIO_NEW_ADDRESS_BILLING = (By.NAME,
                                 'payment_address')
    RADIO_ADDRESS_DELIVERY = (By.XPATH,
                              '//*[@id="collapse-shipping-address"]/div/form/div[3]/label/input')
    BTN_CONTINUE_S_2 = (By.ID, 'button-payment-address')
    BTN_CONTINUE_S_3 = (By.ID, 'button-shipping-address')
    BTN_CONTINUE_S_4 = (By.ID, 'button-shipping-method')
    BTN_CONTINUE_S_5 = (By.ID, 'button-payment-method')
    TERMS_S_5 = (By.XPATH, '//*[@id="collapse-payment-method"]/div/div[2]/div/input[1]')
    BTN_CONFIRM_ORDER = (By.ID, 'button-confirm')

    FIRST_NAME_SHIPPING = (By.ID, 'input-shipping-firstname')
    LAST_NAME_SHIPPING = (By.ID, 'input-shipping-lastname')

    COMPANY_SHIPPING = (By.ID, 'input-shipping-company')
    ADDRESS_1_SHIPPING = (By.ID, 'input-shipping-address-1')
    ADDRESS_2_SHIPPING = (By.ID, 'input-shipping-address-2')
    CITY_SHIPPING = (By.ID, 'input-shipping-city')
    POST_CODE_SHIPPING = (By.ID, 'id="input-shipping-postcode"')
    COUNTRY_SHIPPING = (By.ID, 'input-shipping-country')
    REGION_OR_STATE_SHIPPING = (By.ID, 'input-shipping-zone')
