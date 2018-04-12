
import pytest

from helpers.settings import BASE_HOST, PRODUCT
from pages.cart import CartPage
from pages.home import HomePage


@pytest.allure.step('Test staying on Home Page.')
def test_goto_home_page(init_driver):
        init_driver.get(BASE_HOST)
        assert HomePage(init_driver).is_on_home_page()


@pytest.allure.severity(pytest.allure.severity_level.MINOR)
@pytest.allure.step('Test whether Cart Page is empty.')
def test_empty_cart_page(init_driver):
        init_driver.get(BASE_HOST)
        assert (HomePage(init_driver)
                .goto_cart()
                .is_cart_empty())


@pytest.allure.step('Test whether iPhone was added to cart')
def test_add_iphone_to_cart(init_driver):
        init_driver.get(BASE_HOST)
        assert (HomePage(init_driver)
                .click_nav_phones()
                .goto_product_page(PRODUCT)
                .add_to_cart()
                .goto_cart()
                .is_product_added(PRODUCT))


@pytest.allure.step('Test whether CartButton is empty by default.')
def test_is_cartbutton_empty(init_driver):
        init_driver.get(BASE_HOST)
        assert (HomePage(init_driver)
                .grey_cart_btn
                .click_btn_grey_cart()
                .is_cart_btn_empty())


@pytest.allure.step('Test clicking on the View link after adding product.')
def test_view_cart_link(init_driver):
        init_driver.get(BASE_HOST)
        (HomePage(init_driver)
         .click_nav_phones()
         .goto_product_page(PRODUCT)
         .add_to_cart()
         .grey_cart_btn
         .click_btn_grey_cart()
         .click_link_viewcart())
        assert CartPage(init_driver).is_on_cart_page()


@pytest.allure.step('Testing editing product qantity on Cart Page.')
def test_edit_product_qty(init_driver):
        init_driver.get(BASE_HOST)
        assert (HomePage(init_driver)
                .click_nav_phones()
                .goto_product_page(PRODUCT)
                .add_to_cart()
                .goto_cart()
                .edit_qty_field(3))
