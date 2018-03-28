from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from models.basepage import BasePage
# from models.productpage import ProductPage
# from models.checkoutpage import CheckoutPage

class TestPurchase():

    def test_purchase(self):
        # precondition
        product_page = BasePage(webdriver.Chrome()).go_to_product()
        cart_page = product_page.add_to_cart().go_to_cart()

        checkout_page = cart_page.go_to_checkout()
        order = checkout_page\
                .checkout_options('guest')\
                .add_billing_details()\
                .add_payment_method()\
                .confirm_order()\
                .create_order_obj()

        #compare the order obj with the order from the order database

        #postcondition: delete the order fron the order database

    # self.driver.close()