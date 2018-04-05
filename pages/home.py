"""
Home Page comes here.
"""
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators.base import BasePageLocators
from locators.home import HomePageLocators
from .cart import CartPage
from .login import LoginPage
from .products import ProductsPage
from .base import BasePage


class HomePage(BasePage):
    """
    Home Page methods come here.
    """

    def goto_login(self):
        """
        Go to Login Page.
        """
        self.driver.find_element(*BasePageLocators.MY_ACCOUNT_DROPDOWN).click()
        self.driver.find_element(*BasePageLocators.GO_LOGIN).click()
        return LoginPage(self.driver)

    def is_on_home_page(self):
        """
        Make sure we on Home Page.
        """
        if self.driver.current_url == "https://demo.opencart.com/":
            return True
        return False

    def goto_cart(self):
        """
        Go to Cart Page.
        """
        self.driver.find_element(*BasePageLocators.GO_CART).click()
        return CartPage(self.driver)

    def click_nav_components(self):
        """
        Click Component Tab.
        """
        self.driver.find_element(*HomePageLocators.COMPONENTS_TAB).click()
        return self

    def click_nav_components_monitors(self):
        """
        Click Component Tab.
        Click Monitors.
        """
        self.click_nav_components()
        monitors = self.driver.find_element(*HomePageLocators.MONITORS)
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.element_to_be_clickable(HomePageLocators.MONITORS))
        monitors.click()
        return ProductsPage(self.driver)

    def click_nav_phones(self):
        """
        Click Phones Tab.
        """
        phones = self.driver.find_element(*HomePageLocators.PHONES)
        phones.click()
        return ProductsPage(self.driver)

    def click_nav_desktops(self):
        """
        Click Desktops Tab.
        """
        self.driver.find_element(*HomePageLocators.DESKTOPS).click()
        return self

    def click_nav_desktops_mac(self):
        """
        Click Desktops Tab.
        Click Mac.
        """
        self.click_nav_desktops()
        self.driver.find_element(*BasePageLocators.MAC).click()
        return ProductsPage(self.driver)
