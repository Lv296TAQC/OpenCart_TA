import pytest
from selenium import webdriver
from OpenCart_TA.models.page_objects.home_page import HomePage
from OpenCart_TA.models.page_objects.search_products import SearchProduct
from OpenCart_TA.models.page_objects.shopping_cart_page import EmptyShoppingCart

# class TestCart:
#
#     driver = webdriver.Chrome()
#
#     def test_cart_tab():
#         main_page = HomePage(driver)
#         main_page.navigate_to_home_page().click_on_shoping_cart_tab()
#         assert main_page.is_on_home_page()
#
#     def test_empty_cart():
#         cart = EmptyShoppingCart(driver)
#         cart.navigate_to_home_page().click_on_shoping_cart_tab()
#         assert cart.is_cart_empty()

driver = webdriver.Chrome()

# page = SearchProduct(driver)
# page.navigate_to_home_page().click_on_components_tab()
# page.click_on_monitors()
# page.add_to_cart()


page = SearchProduct(driver)
page.navigate_to_home_page().click_on_components_tab()
page.click_on_monitors()
page.add_to_cart()

