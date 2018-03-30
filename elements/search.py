"""
TODO
"""
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators.search import SearchPageLocators
from .base import BasePageElement


class SearchPageElements(BasePageElement):
    """
    TODO
    """

    def get_search_field_element(self):
        """
        TODO
        """
        return self.driver.find_element(*SearchPageLocators.SEARCH_FIELD)

    def get_search_button_element(self):
        """
        TODO
        """
        return self.driver.find_element(*SearchPageLocators.SEARCH_FIELD)

    def get_search_results(self):
        """
        TODO
        """
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(SearchPageLocators.SEARCH_RESULTS))
            return element
        except NoSuchElementException:
            return None
