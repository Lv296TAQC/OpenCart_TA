from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from elements.base import BasePageElement
from elements.button import Button
from locators.checkout import CheckoutPageLocators


class BillingDetails(BasePageElement):

    def __init__(self, driver):
        super().__init__(driver)

        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(CheckoutPageLocators.FIRST_NAME))

        self.firstname = self.driver.find_element(*CheckoutPageLocators.FIRST_NAME)
        self.lastname = self.driver.find_element(*CheckoutPageLocators.LAST_NAME)
        self.email = self.driver.find_element(*CheckoutPageLocators.EMAIL)
        self.telephone = self.driver.find_element(*CheckoutPageLocators.TELEPHONE)
        self.fax = self.driver.find_element(*CheckoutPageLocators.FAX)

        self.company = self.driver.find_element(*CheckoutPageLocators.COMPANY)
        self.address_1 = self.driver.find_element(*CheckoutPageLocators.ADDRESS_1)
        self.address_2 = self.driver.find_element(*CheckoutPageLocators.ADDRESS_2)
        self.city = self.driver.find_element(*CheckoutPageLocators.CITY)
        self.post_code = self.driver.find_element(*CheckoutPageLocators.POST_CODE)
        self.contry = self.driver.find_element(*CheckoutPageLocators.COUNTRY)
        self.region_or_state = self.driver.find_element(*CheckoutPageLocators.REGION_OR_STATE)

        self.btn = Button(self.driver, CheckoutPageLocators.BTN_GUEST)
