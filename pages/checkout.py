"""
Checkout Page comes here.
"""
from faker import Faker

from elements.accordion.guest.billingdetails import BillingDetailsGuest
from elements.accordion.guest.checkoutoptions import CheckoutOptionsGuest
from elements.accordion.guest.deliverymethod import DeliveryMethodGuest
from elements.accordion.guest.paymentmethod import PaymentMethodGuest
from elements.accordion.user.billingdetails import BillingDetailsUser
from elements.accordion.user.checkoutoptions import CheckoutOptionsUser
from elements.accordion.user.deliverydetails import DeliveryDetailsUser
from elements.accordion.user.deliverymethod import DeliveryMethodUser
from elements.accordion.user.paymentmethod import PaymentMethodUser
from elements.button import Button
from locators.checkout import CheckoutPageLocators
from pages.base import BasePage

# pylint: disable=invalid-name
fake = Faker()


# pylint: disable=no-member
# pylint: disable=attribute-defined-outside-init
class CheckoutPage(BasePage):
    """
    Checkout Page methods come here.
    """

    def checkout_options_g(self) -> "CheckoutPage":
        """
        Fill checkout options
        """
        self.accordion = CheckoutOptionsGuest(self.driver)
        self.accordion.guest_account.click()
        self.accordion.btn_account.click()
        return self

    def add_billing_details_g(self) -> "CheckoutPage":
        """
        Fill billing details
        """

        self.accordion = BillingDetailsGuest(self.driver)
        self.accordion.firstname.send_keys(fake.first_name())
        self.accordion.lastname.send_keys(fake.last_name())
        self.accordion.email.send_keys(fake.ascii_safe_email())
        self.accordion.telephone.send_keys(fake.phone_number())

        self.accordion.company.send_keys(fake.name())
        self.accordion.address_1.send_keys(fake.name())
        self.accordion.address_2.send_keys(fake.name())
        self.accordion.city.send_keys(fake.name())
        self.accordion.post_code.send_keys(fake.isbn10(separator=""))
        self.accordion.contry.click()
        self.accordion.contry.find_element_by_xpath(
            '//*[@id="input-payment-country"]/option[2]').click()
        self.accordion.region_or_state.click()
        self.accordion.region_or_state.find_element_by_xpath(
            '//*[@id="input-payment-zone"]/option[2]').click()
        self.accordion.btn.click()
        return self

    def delivery_method_g(self) -> "CheckoutPage":
        """
        Choose delivery method
        """
        self.accordion = DeliveryMethodGuest(self.driver)
        self.accordion.btn.click()
        return self

    def payment_method_g(self) -> "CheckoutPage":
        """
        Choose payment method
        """
        self.accordion = PaymentMethodGuest(self.driver)
        self.accordion.agree.click()
        self.accordion.btn.click()
        return self

    def checkout_options_u(self) -> "CheckoutPage":
        """
        Fill checkout options for registered user
        """
        self.accordion = CheckoutOptionsUser(self.driver)
        self.accordion.email_field.send_keys('Nick123@gmail.com')
        self.accordion.pass_field.send_keys('123123123')
        self.accordion.btn_login.click()
        return self

    def choose_new_address(self) -> "CheckoutPage":
        """
        Choose new address billing details radio button
        """
        self.accordion = BillingDetailsUser(self.driver)
        self.accordion.btn_new_address.click()
        return self

    def add_billing_details_u(self) -> "CheckoutPage":
        """
        Fill billing details for users
        """
        self.accordion = BillingDetailsUser(self.driver)
        self.accordion.firstname.send_keys(fake.first_name())
        self.accordion.lastname.send_keys(fake.last_name())
        self.accordion.company.send_keys(fake.name())
        self.accordion.address_1.send_keys(fake.name())
        self.accordion.address_2.send_keys(fake.name())
        self.accordion.city.send_keys(fake.name())
        self.accordion.post_code.send_keys(fake.isbn10(separator=""))
        self.accordion.contry.click()
        self.accordion.contry.find_element_by_xpath(
            '//*[@id="input-payment-country"]/option[3]').click()
        self.accordion.region_or_state.click()
        self.accordion.region_or_state.find_element_by_xpath(
            '//*[@id="input-payment-zone"]/option[2]').click()
        self.accordion.btn.click()
        return self

    def choose_new_address_delivery(self) -> "CheckoutPage":
        """
        Choose new address delivery radio button
        """
        self.accordion = DeliveryDetailsUser(self.driver)
        self.accordion.btn_new_address_delivery.click()
        return self

    def add_delivery_details_u(self) -> "CheckoutPage":
        """
        Fill delivery details for users
        """
        self.accordion = DeliveryDetailsUser(self.driver)
        self.accordion.firstname.send_keys(fake.first_name())
        self.accordion.lastname.send_keys(fake.last_name())
        self.accordion.company.send_keys(fake.name())
        self.accordion.address_1.send_keys(fake.name())
        self.accordion.address_2.send_keys(fake.name())
        self.accordion.city.send_keys(fake.name())
        self.accordion.country.click()
        self.accordion.country.find_element_by_xpath(
            '//*[@id="input-shipping-country"]/option[7]').click()
        self.accordion.region_or_state.click()
        self.accordion.region_or_state.find_element_by_xpath(
            '//*[@id="input-shipping-zone"]/option[3]').click()
        self.accordion.btn.click()
        return self

    def delivery_method_u(self) -> "CheckoutPage":
        """
        Press continue button on delivery method
        """
        self.accordion = DeliveryMethodUser(self.driver)
        self.accordion.btn_s_4.click()
        return self

    def payment_method_u(self) -> "CheckoutPage":
        """
        Press continue button on payment method
        """
        self.accordion = PaymentMethodUser(self.driver)
        self.accordion.btn_agree.click()
        self.accordion.btn_continue.click()
        return self

    def confirm_order(self) -> "CheckoutPage":
        """
        Confirm order
        """
        Button(self.driver, CheckoutPageLocators.BTN_CONFIRM_ORDER).click()
        return self
