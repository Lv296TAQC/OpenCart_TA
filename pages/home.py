"""
Home Page comes here.
"""
from urllib.parse import urlparse

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators.base import BasePageLocators
from .cart import CartPage
from .login import LoginPage
from .products import ProductsPage
from .base import BasePage


# pylint: disable=too-many-public-methods
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
        current_url_path = urlparse(self.driver.current_url).path
        if current_url_path == "/opencart.com/":
            return True
        return False

    def goto_cart(self) -> "HomePage":
        """
        Go to Cart Page.
        :return:self
        """
        self.driver.find_element(*BasePageLocators.GO_CART).click()
        return CartPage(self.driver)

    def click_nav_components(self) -> "HomePage":
        """
        Click Component Tab.
        :return:self
        """
        self.driver.find_element(*BasePageLocators.COMPONENTS).click()
        return self

    def click_nav_components_monitors(self):
        """
        Click Component Tab.
        Click Monitors.
        """
        self.click_nav_components()
        monitors = self.driver.find_element(*BasePageLocators.MONITORS)
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.element_to_be_clickable(BasePageLocators.MONITORS))
        monitors.click()
        return ProductsPage(self.driver)

    def click_nav_phones(self) -> ProductsPage:
        """
        Click Phones Tab.
        :return:driver
        """
        self.driver.find_element(*BasePageLocators.PHONES).click()

        return ProductsPage(self.driver)

    def click_nav_desktops(self) -> object:
        """
        Click Desktops Tab.

        :return: Home Page with clicked Desktops Navigation Bar.
        """
        self.logger.info('clicking top Navigation Desktops Bar')
        self.driver.find_element(*BasePageLocators.DESKTOPS).click()
        return self

    def click_nav_laptops(self) -> "HomePage":
        """
        Click Laptops Tab.
        :return:self
        """
        self.driver.find_element(*BasePageLocators.LAPTOPS).click()
        return self

    def click_nav_tablets(self) -> ProductsPage:
        """
        Click Tablests Tab.
        :return:driver
        """
        self.driver.find_element(*BasePageLocators.TABLETS).click()
        return ProductsPage(self.driver)

    def click_nav_cameras(self) -> ProductsPage:
        """
        Click Cameras Tab.
        :return:driver
        """
        self.driver.find_element(*BasePageLocators.CAMERAS).click()
        return ProductsPage(self.driver)

    def click_nav_mp3_players(self) -> "HomePage":
        """
        Click MP3 Players Tab.
        :return:self
        """
        self.driver.find_element(*BasePageLocators.MP3S).click()
        return self

    def click_nav_desktops_pc(self) -> ProductsPage:
        """
        Click Desktops Tab.
        Click Pc.
        :return:driver
        """
        self.click_nav_desktops()
        self.driver.find_element(*BasePageLocators.PC).click()
        return ProductsPage(self.driver)

    def click_nav_desktops_mac(self) -> object:
        """
        Click Desktops Tab.
        Click Mac.

        :return: Products MAC Page Object
        """
        self.logger.info('clicking top navigation for getting to the Desktops->MAC Products Page')
        self.click_nav_desktops()
        self.driver.find_element(*BasePageLocators.MAC).click()
        return ProductsPage(self.driver)

    def click_nav_desktops_show_all(self) -> ProductsPage:
        """
        Click Desktops Tab.
        Click Show all desktops.
        :return:driver
        """
        self.click_nav_desktops()
        self.driver.find_element(*BasePageLocators.ALLDESKTOPS).click()
        return ProductsPage(self.driver)

    def click_nav_laptops_macs(self) -> ProductsPage:
        """
        Click Laptops Tab.
        Click Macs.
        :return:driver
        """
        self.click_nav_laptops()
        self.driver.find_element(*BasePageLocators.MACS).click()
        return ProductsPage(self.driver)

    def click_nav_laptops_windows(self) -> ProductsPage:
        """
        Click Laptops Tab.
        Click Windows.
        :return:driver
        """
        self.click_nav_laptops()
        self.driver.find_element(*BasePageLocators.WINDOWS).click()
        return ProductsPage(self.driver)

    def click_nav_laptops_show_all(self) -> ProductsPage:
        """
        Click Laptops Tab.
        Click Show all Laptops .
        :return:driver
        """
        self.click_nav_laptops()
        self.driver.find_element(*BasePageLocators.ALLLEPTOPS).click()
        return ProductsPage(self.driver)

    def click_nav_components_mice(self) -> ProductsPage:
        """
        Click Components Tab.
        Click Mice .
        :return:driver
        """
        self.click_nav_components()
        self.driver.find_element(*BasePageLocators.MICE).click()
        return ProductsPage(self.driver)

    def click_nav_components_printers(self) -> ProductsPage:
        """
        Click Components Tab.
        Click Printers .
        :return:driver
        """
        self.click_nav_components()
        self.driver.find_element(*BasePageLocators.PRINTERS).click()
        return ProductsPage(self.driver)

    def click_nav_components_scanners(self) -> ProductsPage:
        """
        Click Components Tab.
        Click Scanners.
        :return:driver
        """
        self.click_nav_components()
        self.driver.find_element(*BasePageLocators.SCANNERS).click()
        return ProductsPage(self.driver)

    def click_nav_components_webcamera(self) -> ProductsPage:
        """
        Click Components Tab.
        Click Web Camera.
        :return:driver
        """
        self.click_nav_components()
        self.driver.find_element(*BasePageLocators.WEBCAMERAS).click()
        return ProductsPage(self.driver)

    def click_nav_components_show_all(self)->ProductsPage:
        """
        Click Components Tab.
        Click Show all components.
        :return:driver
        """
        self.click_nav_components()
        self.driver.find_element(*BasePageLocators.ALLCOMPONENTS).click()
        return ProductsPage(self.driver)

    def get_components_list(self) -> list:
        """
        Find all subcategory Components
        :return:subcategory components
        """

        components_list = self.driver.find_elements(*BasePageLocators.LIST_COMPONENS)
        return components_list

    def get_desktops_list(self) -> list:
        """
        Find all subcategory Desktops
        :return:subcategory desktops
        """

        desktops_list = self.driver.find_elements(*BasePageLocators.LIST_DESKTOPS)
        return desktops_list

    def get_laptops_list(self) -> list:
        """
        Find all subcategory Laptops
        :return:subcategory laptops
        """

        laptops_list = self.driver.find_elements(*BasePageLocators.LIST_LAPTOPS)
        return laptops_list

    def title(self) -> str:
        """
        find the page name
        :return:page title
        """
        return self.driver.title
