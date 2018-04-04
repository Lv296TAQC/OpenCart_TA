"""
In this module class BasePage constructor will take argument driver,
which has to be returned by DriverFactory().create_web_driver(driver_name)
method
"""

from selenium import webdriver


class BasePage:
    """Base class to initialize the base page that will be called from all pages"""

    def __init__(self, driver=None):
        """
        Initialization of base driver
        """
        self.driver = driver if driver else webdriver.Chrome()
        self.driver.get("https://demo.opencart.com/")
