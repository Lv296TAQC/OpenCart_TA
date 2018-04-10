"""
Base Page comes here.
"""
import logging
import logging.config
from selenium import webdriver

from locators.base import BasePageLocators


# pylint: disable=too-few-public-methods
class BasePage:
    """
    Base class to initialize the base page that will be called from all pages.
    """

    def __init__(self, driver=None):
        """
        Initialization of base driver.

        :param driver: Receives driver with default value None.
        """
        self.driver = driver if driver else webdriver.Chrome()
        self.grey_cart_btn = GreyCartBtn(driver)

    logger = logging.getLogger(__name__)  # This is not set up yet,but need to be here (pylint)


class GreyCartBtn:
    """
    Class to work with grey Cart button.
    """
    def __init__(self, driver):
        """
        Initialization of grey Cart Button.

        :param driver: Well, it's driver.
        """
        self.driver = driver

    def click_btn_grey_cart(self) -> object:
        """
        Make webdriver click grey Cart button.

        :return: Home Page Object with clicked grey Cart button.
        """
        BasePage.logger.info('clicking grey Cart button')
        self.driver.find_element(*BasePageLocators.BTN_GREY_CART).click()
        return self

    def click_link_viewcart(self) -> object:
        """
        Make webdriver click Viewcart Link in grey Cart button.

        :return: Home Page Object with clicked Viewcart link.
        """
        BasePage.logger.info('clicking Viewcart link')
        self.driver.find_element(*BasePageLocators.LINK_VIEW_CART).click()
        return self

    def click_link_checkout(self) -> object:
        """
        Make webdriver click Checkout Link in grey Cart button.

        :return: Home Page Object with clicked Checkout link.
        """
        BasePage.logger.info('clicking Checkout link')
        self.driver.find_element(*BasePageLocators.LINK_CHECKOUT).click()
        return self
