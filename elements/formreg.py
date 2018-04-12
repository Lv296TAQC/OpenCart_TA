""" account register form"""
from helpers.singleton import Wrapper
from locators.login import LoginPageLocators
from locators.register import RegisterElementLocators
from locators.register import ErorsRegisterElement


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


class ERORELEMENR(Element):
    """reload get and set metods """

    def __get__(self, eobj, cls=None):
        eror_text = Wrapper().conection.find_element(self.metod, self.locator).text
        return eror_text


# pylint: disable=too-few-public-methods
class Reg:
    """Init class elements form account register"""
    url_login = 'http://localhost/opencart/index.php?route=account/login'
    url = 'http://localhost/opencart/index.php?route=account/register'
    first_name = FormsElement(*RegisterElementLocators.FIRSTNAME)
    last_name = FormsElement(*RegisterElementLocators.LASTNAME)
    e_mail = FormsElement(*RegisterElementLocators.EMAIL)
    telephone = FormsElement(*RegisterElementLocators.TELEPHONE)
    password = FormsElement(*RegisterElementLocators.PASSWORD)
    confir_password = FormsElement(*RegisterElementLocators.CONFIRMPASSWORD)
    agri_checkbox = FormsElement(*RegisterElementLocators.AGRI)
    continue_btn = FormsElement(*RegisterElementLocators.CONTINUE)
    telephone_error = ERORELEMENR(*ErorsRegisterElement.ETELEPHONE)
    first_name_error = ERORELEMENR(*ErorsRegisterElement.EFIRSTNAME)
    last_name_error = ERORELEMENR(*ErorsRegisterElement.ELASTNAME)
    e_mail_error = ERORELEMENR(*ErorsRegisterElement.EEMAIL)
    password_error = ERORELEMENR(*ErorsRegisterElement.EPASSWORD)
    password_confirm_error = ERORELEMENR(*ErorsRegisterElement.ECONFIRMPASSWORD)
    title_error = ERORELEMENR(*ErorsRegisterElement.ETITLE)
    input_passwd = FormsElement(*LoginPageLocators.PASSWORD_INPUT_FIELD)
    input_email = FormsElement(*LoginPageLocators.EMAIL_INPUT_FIELD)
    login_btn = FormsElement(*LoginPageLocators.LOGIN_BUTTON)

    def open(self) -> None:
        """
        Open register page
        :return: none
        """
        Wrapper().webdriver_rem().get(self.url)

    @staticmethod
    def close() -> None:
        """
        Close driver
        :return:none
        """
        Wrapper().conection.close()

    def login(self):
        """
        Open register page
        :return: none
        """
        Wrapper().webdriver_rem().get(self.url_login)

    @staticmethod
    def title() -> str:
        """
        find title page
        :return: title
        """
        return Wrapper().conection.title
