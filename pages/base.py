"""
Base Page comes here.
"""

from selenium import webdriver


# pylint: disable=too-few-public-methods
class BasePage:
    """
    Base class to initialize the base page that will be called from all pages
    """

    def __init__(self, driver=None):
        """
        Initialization of base driver
        """
        self.driver = driver if driver else webdriver.Chrome()
