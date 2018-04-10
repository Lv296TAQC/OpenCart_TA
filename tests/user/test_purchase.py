import allure
import pytest
from selenium import webdriver

from helpers.local_settings import BASE_HOST
from pages.product import ProductPage

url = BASE_HOST + "index.php?route=product/product&product_id=47"

driver = webdriver.Chrome()
driver.get(url)
checkout_page = ProductPage(driver).add_to_cart().goto_cart().goto_checkout()


@pytest.allure.BLOCKER
@allure.step('The user is logged in')
def test_checkout_options():
    assert checkout_page.checkout_options_u()


@pytest.allure.BLOCKER
@allure.step('User fills in personal data')
def test_add_billing_details():
    assert checkout_page.choose_new_address().add_billing_details_u()


@allure.step('The user fills in the data to send the goods')
def test_add_delivery_details():
    assert checkout_page.choose_new_address_delivery().add_delivery_details_u()


def test_delivery_method():
    assert checkout_page.delivery_method_u()


def test_payment_method():
    assert checkout_page.payment_method_u()


def test_confirm():
    assert checkout_page.confirm_order()
