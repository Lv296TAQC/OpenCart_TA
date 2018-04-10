"""
Checkout Page comes here.
"""

from faker import Faker

from elements.accordion.billingdetails import BillingDetails
from elements.accordion.checkoutoptions import CheckoutOptions
from elements.accordion.deliverydetails import DeliveryDetails
from pages.base import BasePage

# pylint: disable=invalid-name
fake = Faker()


# pylint: disable=no-member
# pylint: disable=attribute-defined-outside-init
class CheckoutPage(BasePage):
    """
    Checkout Page methods come here.
    """

    def checkout_options(self):
        """
        Fill checkout options
        """
        self.accordion = CheckoutOptions(self.driver)
        self.accordion.guest_account.click()
        self.accordion.btn_account.click()
        return self

    def checkout_options_users(self):
        """
        Fill checkout options for registered user
        """
        self.accordion = CheckoutOptions(self.driver)
        self.accordion.email_field.send_keys('Nick123@gmail.com')
        self.accordion.pass_field.send_keys('123123123')
        self.accordion.btn_login.click()
        return self

    def choose_new_address(self):
        """
        Choose new address radio button
        """
        self.accordion = BillingDetails(self.driver)
        self.accordion.btn_new_address.click()

    def add_billing_details(self):
        """
        Fill billing details
        """

        self.accordion = BillingDetails(self.driver)
        self.accordion.firstname.send_keys(fake.first_name())
        self.accordion.lastname.send_keys(fake.last_name())
        self.accordion.email.send_keys(fake.ascii_safe_email())
        self.accordion.telephone.send_keys(fake.phone_number())
        self.accordion.fax.send_keys(fake.phone_number())

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

    def add_payment_method(self):
        """
        Fill shipping details
        """
        self.accordion = DeliveryDetails(self.driver)
        self.accordion.firstname.send_keys(fake.first_name())
        self.accordion.lastname.send_keys(fake.last_name())

        self.accordion.company.send_keys(fake.name())
        self.accordion.address_1.send_keys(fake.name())
        self.accordion.address_2.send_keys(fake.name())
        self.accordion.city.send_keys(fake.name())
        self.accordion.post_code.send_keys(fake.name())
        self.accordion.country.send_keys(fake.name())
        self.accordion.country.send_keys(fake.name())
        self.accordion.region_or_state.send_keys(fake.name())
        return self

    def confirm_order(self):
        """
        TODO
        """

    def create_order_obj(self):
        """
        TODO
        """
