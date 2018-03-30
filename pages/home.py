"""
TODO
"""
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.home import HomePageLocators
from .base import BasePage


class HomePage(BasePage):
    """
    TODO
    """

    def logging(self):
        """
        TODO
        """
        self.driver.find_element_by_xpath('//*[@id="top-links"]/ul/li[2]/a').click()
        self.driver.find_element_by_xpath('//*[@id="top-links"]/ul/li[2]/ul/li[2]/a').click()

    def input_email(self):
        """
        TODO
        """
        self.driver.find_element_by_id('input-email').send_keys('Nick123@gmail.com')

    def input_password(self):
        """
        TODO
        """
        self.driver.find_element_by_id('input-password').send_keys('123123123')

    def login(self):
        """
        TODO
        """
        self.driver.find_element_by_xpath('//*[@id="content"]/div/div[2]/div/form/input').click()

    def navigate_to_home_page(self):
        """
        TODO
        """
        self.driver.get("http://127.0.0.1/opencart.com")
        return self

    def is_on_home_page(self):
        """
        TODO
        """
        if self.driver.current_url == "http://127.0.0.1/opencart.com":
            return True
        return False

    def click_on_shoping_cart_tab(self):
        """
        TODO
        """
        cart_tab = self.driver.find_element(*HomePageLocators.SHOPPING_CART_TAB)
        cart_tab.click()

    def click_on_components_tab(self):
        """
        TODO
        """
        components_tab = self.driver.find_element(*HomePageLocators.COMPONENTS_TAB)
        components_tab.click()

    def click_on_monitors(self):
        """
        TODO
        """
        monitors = self.driver.find_element(*HomePageLocators.MONITORS)
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.element_to_be_clickable((HomePageLocators.MONITORS)))
        monitors.click()

    def click_on_phones_tab(self):
        """
        TODO
        """
        phones = self.driver.find_element(*HomePageLocators.PHONES)
        phones.click()

    def go_to_product(self):
        """
        TODO
        """
        self.driver.get('http://localhost/index.php?route=product/product&product_id=41')

    def select_mac_product(self):
        """Make webdriver click Mac product."""
        self.driver.find_element_by_xpath('//*[@id="menu"]/div[2]/ul/li[1]/a').click()
        self.driver.find_element_by_xpath(
            '//*[@id="menu"]/div[2]/ul/li[1]/div/div/ul/li[2]/a').click()

    def add_mac_to_cart(self):
        """Make webdriver add Mac product to Cart."""
        self.driver.find_element_by_xpath('//*[@id="content"]/div[2]/div/div/div[1]/a/img').click()
        self.driver.find_element_by_id("button-cart").click()
