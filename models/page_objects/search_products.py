from OpenCart_TA.models.locators import SearchProductLocators
from OpenCart_TA.models.page_objects.home_page import HomePage


class SearchProduct(HomePage):
    def add_to_cart(self):
        add_to_cart_button = self.driver.find_element(*SearchProductLocators.ADD_APPLE_CINEMA)
        add_to_cart_button.click()
