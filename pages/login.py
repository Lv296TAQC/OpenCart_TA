"""
TODO
"""
from pages.base import BasePage


class LoginPage(BasePage):
    """
    TODO
    """

    def input_email(self):
        """Make webdriver set 'E-Mail' value."""
            # self.driver.driver.find_element_by_id("input-email").\
            #     send_keys(RegistrationPage.last_created_email)
        self.driver.find_element_by_id("input-email").send_keys('oleksandr.makar.ol@gmail.com')

    def input_password(self):
        """Make webdriver set 'Password' value."""
        #     self.driver.driver.find_element_by_id("input-password").\
        # send_keys(RegistrationPage.last_created_password)
        self.driver.find_element_by_id("input-password").send_keys('saxon123')

    def login(self):
        """Make webdriver initiate login by click 'Login' Button"""
        self.driver.find_element_by_xpath('//*[@id="content"]/div/div[2]/div/form/input').click()
