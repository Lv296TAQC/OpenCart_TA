from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from models.basepage import BasePage
from models.locators import CheckoutPageLocators


class CheckoutPage(BasePage):

    def checkout_options(self):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(CheckoutPageLocators.STEP_ONE_CONTINUE))

        element = self.driver.find_element(*CheckoutPageLocators.GUEST_ACCOUNT)
        element.click()

        element = self.driver.find_element(*CheckoutPageLocators.STEP_ONE_CONTINUE)
        element.click()

    def add_billing_details(self):
        pass

    def add_payment_method(self):
        pass

    def confirm_order(self):
        pass

    def create_order_obj(self):
        pass
