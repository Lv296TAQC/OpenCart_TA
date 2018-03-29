from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from OpenCart_TA.models.locators import HomePageLocators
from OpenCart_TA.models.page_objects.base_page import BasePage


class HomePage(BasePage):
    def to_home_page(self):
        self.driver.get("http://127.0.0.1/")
        return self

    def logging(self):
        self.driver.find_element_by_xpath('//*[@id="top-links"]/ul/li[2]/a').click()
        self.driver.find_element_by_xpath('//*[@id="top-links"]/ul/li[2]/ul/li[2]/a').click()

    def input_email(self):
        self.driver.find_element_by_id('input-email').send_keys('Nick123@gmail.com')

    def input_password(self):
        self.driver.find_element_by_id('input-password').send_keys('123123123')

    def login(self):
        self.driver.find_element_by_xpath('//*[@id="content"]/div/div[2]/div/form/input').click()

    def navigate_to_home_page(self):
        self.driver.get("http://127.0.0.1/opencart.com")
        return self

    def is_on_home_page(self):
        if self.driver.current_url == "http://127.0.0.1/opencart.com":
            return True
            print(True)
        print(False)
        return False

    def click_on_shoping_cart_tab(self):
        cart_tab = self.driver.find_element(*HomePageLocators.SHOPPING_CART_TAB)
        cart_tab.click()

    def click_on_components_tab(self):
        components_tab = self.driver.find_element(*HomePageLocators.COMPONENTS_TAB)
        components_tab.click()

    def click_on_monitors(self):
        monitors = self.driver.find_element(*HomePageLocators.MONITORS)
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.element_to_be_clickable((HomePageLocators.MONITORS)))
        monitors.click()

    def click_on_phones_tab(self):
        phones = self.driver.find_element(*HomePageLocators.PHONES)
        phones.click()
