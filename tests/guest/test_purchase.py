from selenium import webdriver

from pages.product import ProductPage

driver = webdriver.Chrome()
driver.get('http://oppencart.herokuapp.com/index.php?route=product/product&path=20_27&product_id=41')
checkout_page = (ProductPage(driver).add_to_cart()
                                    .goto_cart()
                                    .goto_checkout())


def test_purchase():
    checkout_page.checkout_options_users()
    checkout_page.add_billing_details()
