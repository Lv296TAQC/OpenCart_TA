from web_pages.basepage import BasePage
from locators.search_page_locators import SearchPageLocators

class SearchPage(BasePage):
    """Home page action methods come here. I.e. Python.org"""

    #Declares a variable that will contain the retrieved text
    search_text_element = SearchTextElement()

    def is_title_matches(self, title):
        """Verifies that some text appears in page title"""
        return title in self.driver.title

    def click_search_button(self):
        """Triggers the search"""
        element = self.driver.find_element(SearchPageLocators.SEARCH_BUTTON)
        element.click()

    def perform_search(self, searched_product):
        pass