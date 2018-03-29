from pages.base import BasePage


class LoginPage(BasePage):

    def go_to_login(self):
        """Make webdriver go to 'Login' Page."""
        self.driver.find_element_by_xpath('//*[@id="top-links"]/ul/li[2]/a').click()
        self.driver.find_element_by_xpath('//*[@id="top-links"]/ul/li[2]/ul/li[2]/a').click()

    def input_email(self):
        """Make webdriver set 'E-Mail' value."""
        #  At this point i'm trying to find solution for implementing forked scenario to have either presetted hard-codded
        #  'E-Mail' and 'Password' values, either values taken from last_created_email and last_created_password variables.

        #     self.driver.driver.find_element_by_id("input-email").send_keys(RegistrationPage.last_created_email)
        self.driver.find_element_by_id("input-email").send_keys('oleksandr.makar.ol@gmail.com')

    def input_password(self):
        """Make webdriver set 'Password' value."""
        #     self.driver.driver.find_element_by_id("input-password").send_keys(RegistrationPage.last_created_password)
        self.driver.find_element_by_id("input-password").send_keys('saxon123')

    def login(self):
        """Make webdriver initiate login by click 'Login' Button"""
        self.driver.find_element_by_xpath('//*[@id="content"]/div/div[2]/div/form/input').click()
