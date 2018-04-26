import pytest

from helpers.constants import Outputs
from pages.cart import CartPage
from pages.home import HomePage
from pages.base import GreyCartBtn
from pages.product import ProductPage

NEW_PRODUCT_QUANTITY = 2
SET_TOO_MUCH_PRODUCT = 999


def test_check_default_cart_empty(login_setup):
    driver = login_setup
    with pytest.allure.step('Testing that Cart is empty by default'):
        GreyCartBtn(driver)\
            .click_btn_grey_cart()\
            .is_cart_btn_empty()


def test_add_goods_to_cart(login_setup):
    driver = login_setup
    with pytest.allure.step('Testing adding products to cart functional'):
        HomePage(driver)\
            .click_nav_desktops_mac()\
            .goto_mac_desktops()\
            .add_to_cart()
        assert (Outputs.TEXT_ALERT_PRODUCT_ADD in
                ProductPage(driver).get_product_add_confirmation())


def test_edit_goods_qty(login_setup):
    driver = login_setup
    with pytest.allure.step('Testing editing products quantity in cart functional'):
        HomePage(driver)\
            .click_nav_desktops_mac()\
            .goto_mac_desktops()\
            .add_to_cart()\
            .goto_cart()\
            .edit_good_qty(NEW_PRODUCT_QUANTITY)
        assert (Outputs.get_edited_product_quantity(NEW_PRODUCT_QUANTITY)
                in HomePage(driver).get_product_quantity())


def test_too_many_goods(login_setup):
    driver = login_setup
    with pytest.allure.step('Testing alert appear after adding too much products to cart'):
        HomePage(driver)\
            .click_nav_desktops_mac()\
            .goto_mac_desktops()\
            .add_to_cart()\
            .goto_cart()\
            .edit_good_qty(SET_TOO_MUCH_PRODUCT)
        assert (Outputs.TEXT_ALERT_TOO_MUCH_PRODUCT in CartPage(driver).get_alert_too_much())


def test_delete_goods_from_cart(login_setup):
    driver = login_setup
    with pytest.allure.step('Testing deleting products from cart functional'):
        HomePage(driver)\
            .click_nav_desktops_mac()\
            .goto_mac_desktops()\
            .add_to_cart()\
            .goto_cart()\
            .delete_good_from_cart()
        assert Outputs.TEXT_ZERO_PRODUCT_QUANTITY in HomePage(driver).get_product_quantity()
