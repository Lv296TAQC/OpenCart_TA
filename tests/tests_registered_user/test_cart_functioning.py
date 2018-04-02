import logging
import pytest
from selenium import webdriver


from pages.home import HomePage
from pages.login import LoginPage
from pages.cart import CartPage
from pages.product import ProductPage

driver = webdriver.Chrome()
base_url = 'http://localhost:1234/opencart.com'
driver.get(base_url)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def test_add_goods_to_cart():
    with pytest.allure.step('Testing adding goods to cart functional'):
        logger.info('Start testing add goods to cart function')
        page = HomePage(driver).logging()
        page = LoginPage(driver).input_password().input_email().login()
        page = HomePage(driver).select_mac_product()
        page = ProductPage(driver).add_mac_to_cart().driver.implicitly_wait(5)
        logger.info('Checking proper work of adding goods to cart')
        success_text = page.driver.find_element_by_class_name('alert')
        assert 'Success: You have added' in success_text.text
        logger.info('Work of adding goods to cart function has been checked')


def test_edit_goods_qty():
    with pytest.allure.step('Testing editing goods quantity in cart functional'):
        logger.info('Start testing edit goods quantity in cart function')
        page = HomePage(driver).click_on_shoping_cart_tab()
        page = CartPage(driver).edit_good_qty()
        logger.info('Checking proper work of editing goods quantity in cart function')
        edited_cart = page.driver.find_element_by_id('cart-total')
        assert '2 item(s)' in edited_cart.text
        logger.info('Work of edit goods quantity in cart function has been checked')


def test_delete_goods_from_cart():
    with pytest.allure.step('Testing deleting goods from cart functional'):
        logger.info('Start testing delete goods from cart function')
        page = CartPage(driver).delete_good_from_cart()
        logger.info('Checking proper work of deleting goods from cart function')
        empty_cart = page.driver.find_element_by_id('cart-total')
        assert '0 item(s)' in empty_cart.text
        logger.info('Work of deleting goods from cart function has been checked')
