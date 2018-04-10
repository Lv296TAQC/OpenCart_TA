"""
Class Button comes here.
"""
from elements.base import BasePageElement


# pylint: disable=too-few-public-methods
class Button(BasePageElement):
    """
    Button methods come here.
    """

    def __init__(self, driver, locator):
        """
        Add locator property

        :param driver: state of driver
        :param locator: tuple contains attribute available for By class and the same locator
        """
        super().__init__(driver)
        self.locator = locator

    def click(self):
        """
        Click on the button defined by the locator
        """
        self.driver.find_element(*self.locator).click()
