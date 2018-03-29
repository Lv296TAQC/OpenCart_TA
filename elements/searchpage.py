from selenium.common.exceptions import NoSuchElementException

from locators.searchpage import SearchPageLocators
from helpers.driver_factory import DriverFactory
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SearchPageElements:

    driver = DriverFactory.create_web_driver("chrome")

    def get_search_field_element(self):
        return self.driver.find_element(*SearchPageLocators.SEARCH_FIELD)

    def get_search_button_element(self):
        return self.driver.find_element(*SearchPageLocators.SEARCH_FIELD)

    def get_search_results(self):
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(*SearchPageLocators.SEARCH_RESULTS))
            return element
        except NoSuchElementException:
            return False
