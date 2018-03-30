"""
TODO
"""
from elements.search import SearchPageElements
from .base import BasePage


class SearchPage(BasePage):
    """Home page action methods come here. I.e. Python.org"""

    # Declare all web elements, present on web page search page
    search_page_element = SearchPageElements()

    def is_title_matches(self, title):
        """Verifies that some text appears in page title"""
        return title in self.driver.title

    def fill_search_field(self, searched_product):
        """
        TODO
        """
        self.search_page_element.get_search_field_element().send_keys(searched_product)

    def click_search_button(self):
        """Triggers the search"""
        self.search_page_element.get_search_button_element().click()

    def perform_search(self, product_name):
        """
        TODO
        """
        self.fill_search_field(product_name)
        self.click_search_button()

    def is_product_matches(self, product_name):
        """
        TODO
        """
        self.perform_search(product_name)
        return self.search_page_element.get_search_results()
