import pytest

from helpers.settings import (BASE_HOST,
                              BASE_USER_EMAIL,
                              BASE_USER_PASSWORD)
from locators.base import BasePageLocators
from locators.cart import CartPageLocators
from locators.product import ProductPageLocators
from pages.cart import CartPage
from pages.home import HomePage
from pages.base import GreyCartBtn


def test_check_default_cart_empty(init_driver):
    _PAGE = None
    driver = init_driver
    driver.get(BASE_HOST)
    with pytest.allure.step('Testing that Cart is empty by default'):
        _PAGE = HomePage(driver)\
            .goto_login()\
            .input_password(BASE_USER_PASSWORD)\
            .input_email(BASE_USER_EMAIL)\
            .login()\
            .goto_homepage()

        _PAGE = GreyCartBtn(driver).\
            click_btn_grey_cart()
        empty_cart = _PAGE.driver.find_element(*BasePageLocators.BTN_GREY_CART)
        assert 'Your shopping cart is empty!' in empty_cart.text


def test_add_goods_to_cart(init_driver):
    driver = init_driver
    with pytest.allure.step('Testing adding goods to cart functional'):
        _PAGE = HomePage(driver)\
            .click_nav_desktops_mac()\
            .goto_mac_desctops()\
            .add_to_cart()
        success_text = _PAGE.driver.find_element(*ProductPageLocators.ALERT)
        assert 'Success: You have added' in success_text.text


def test_edit_goods_qty(init_driver):
    driver = init_driver
    new_qty = 2
    with pytest.allure.step('Testing editing goods quantity in cart functional'):
        _PAGE = HomePage(driver)\
            .goto_cart()\
            .edit_good_qty(new_qty)
        edited_cart = _PAGE.driver.find_element(*BasePageLocators.BTN_GREY_CARD_AMOUNT)
        assert f'{new_qty} item(s)' in edited_cart.text


def test_too_many_goods(init_driver):
    driver = init_driver
    too_much_product = 1000
    with pytest.allure.step('Testing alert appear after adding too much product to cart'):
        _PAGE = CartPage(driver).edit_good_qty(too_much_product)
        error_message = _PAGE.driver.find_element(*CartPageLocators.ALERT_TOO_MUCH_PRODUCT)
        assert 'Products marked with *** are not available' in error_message.text


def test_delete_goods_from_cart(init_driver):
    driver = init_driver
    with pytest.allure.step('Testing deleting goods from cart functional'):
        _PAGE = CartPage(driver)\
            .delete_good_from_cart()
        empty_cart = _PAGE.driver.find_element(*BasePageLocators.BTN_GREY_CARD_AMOUNT)
        assert '0 item(s)' in empty_cart.text
