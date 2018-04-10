from selenium import webdriver

from pages.cart import CartPage
from pages.product import ProductPage

driver = webdriver.Chrome()
driver.get('https://demo.opencart.com/index.php?route=product/product&product_id=47')
checkout_page = ProductPage(driver).add_to_cart()
checkout_page = ProductPage(driver).goto_cart()
checkout_page = CartPage(driver).goto_checkout()


def test_checkout():
    checkout_page.checkout_options_users()
