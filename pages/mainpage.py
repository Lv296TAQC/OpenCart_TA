from pages.base import BasePage


class MainPage(BasePage):

    def select_mac_product(self):
        """Make webdriver click Mac product."""
        self.driver.find_element_by_xpath('//*[@id="menu"]/div[2]/ul/li[1]/a').click()
        self.driver.find_element_by_xpath('//*[@id="menu"]/div[2]/ul/li[1]/div/div/ul/li[2]/a').click()

    def add_mac_to_cart(self):
        """Make webdriver add Mac product to Cart."""
        self.driver.find_element_by_xpath('//*[@id="content"]/div[2]/div/div/div[1]/a/img').click()
        self.driver.find_element_by_id("button-cart").click()
