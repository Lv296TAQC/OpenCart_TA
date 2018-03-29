from elements.basepage import BasePageElement
from locators.searchpage import SearchPageLocators

class SearchPageElements(BasePageElement):
    def __init__(self, driver):
        self.driver = driver

    def get_search_field_element(self):
        driver = self.driver
        SEARCH_FIELD_ELEMENT = driver.find_element(SearchPageLocators.SEARCH_FIELD)
        return SEARCH_FIELD_ELEMENT
