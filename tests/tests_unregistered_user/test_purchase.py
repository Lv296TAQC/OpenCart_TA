import pytest
from selenium import webdriver

from pages.home import HomePage
from pages.product import ProductPage
from pages.cart import CartPage
from pages.checkout import CheckoutPage


class TestPurchase():

    @pytest.fixture()
    def wrap(self):
        self.driver = webdriver.Chrome()
        yield
        self.driver.close()

    def test_purchase(self, wrap):
        # precondition
        driver = self.driver

        page = HomePage(driver)
        page.go_to_product()

        page = ProductPage(driver)
        page.add_to_cart()

        page.go_to_cart()
        # page.cart.click()

        page = CartPage(driver)
        page.go_to_checkout()

        page = CheckoutPage(driver)
        page.checkout_options()
        # page.add_billing_details()
        # page.add_payment_method()
        # page.confirm_order()

        # order = page.create_order_obj()

        #compare the order obj with the order from the order database

        #///////////////////
        #postcondition: delete the order fron the order database
