""" account register form"""
from helpers.singleton import Wrapper
from locators.register import RegisterElementLocators


# pylint: disable=too-few-public-methods
class Element:
    """init clas elements who takes metod By and locators"""

    def __init__(self, metod, locator):
        self.locator = locator
        self.metod = metod


# pylint: disable=too-few-public-methods
class FormsElement(Element):
    """reload get and set metods """

    def __get__(self, obj, cls=None):
        Wrapper().conection.find_element(self.metod, self.locator).click()

    def __set__(self, obj, value):
        """Gets the text of the specified object"""
        Wrapper().conection.find_element(self.metod, self.locator).clear()
        Wrapper().conection.find_element(self.metod, self.locator).send_keys(value)


# pylint: disable=too-few-public-methods
class Reg:
    """Init class elements form account register"""
    url = 'http://localhost/index.php?route=account/register'
    first_name = FormsElement(*RegisterElementLocators.FIRSTNAME)
    last_name = FormsElement(*RegisterElementLocators.LASTNAME)
    e_mail = FormsElement(*RegisterElementLocators.EMAIL)
    telephone = FormsElement(*RegisterElementLocators.TELEPHONE)
    password = FormsElement(*RegisterElementLocators.PASSWORD)
    confir_password = FormsElement(*RegisterElementLocators.CONFIRMPASSWORD)
    agri_checkbox = FormsElement(*RegisterElementLocators.AGRI)
    continue_btn = FormsElement(*RegisterElementLocators.CONTINUE)

    def open(self) -> None:
        """
        Open register page
        :return: none
        """

        Wrapper().webdriver_rem().get(self.url)
