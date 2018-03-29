from pages.base import BasePage
from locators.locators import CartPageLocators


class CartPage(BasePage):

    def go_to_cart(self):
        """Make webdriwer go to 'Cart' Page."""
        self.driver.find_element_by_class_name("fa-shopping-cart").click()

    def edit_good_qty(self):
        """Make webdriver change qty of product in Cart"""
        self.driver.find_element_by_xpath('//*[@id="content"]/form/div/table/tbody/tr/td[4]/div/input').clear()
        self.driver.find_element_by_xpath('//*[@id="content"]/form/div/table/tbody/tr/td[4]/div/input').send_keys('2')
        self.driver.find_element_by_xpath('//*[@id="content"]/form/div/table/tbody/tr/td[4]/div/span/button[1]').click()

    def delete_good_from_cart(self):
        """Make webdriver delete product from Cart."""
        self.driver.find_element_by_xpath('//*[@id="content"]/form/div/table/tbody/tr/td[4]/div/span/button[2]').click()

    def go_to_checkout(self):
        element = self.driver.find_element(*CartPageLocators.GO_CHECKOUT)
        element.click()
