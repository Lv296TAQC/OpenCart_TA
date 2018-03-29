from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from models.driver import MyDriver
from functional.helper import (generate_random_email, get_random_name,
                               get_random_digit, get_random_password)


class RegistrationPage(MyDriver):
    last_created_password = None
    last_created_email = None

    def go_to_registration(self):
        """Make webdriver go to 'Registration' Page."""
        self.driver.find_element_by_xpath('//*[@id="top-links"]/ul/li[2]/a').click()
        self.driver.find_element_by_xpath('//*[@id="top-links"]/ul/li[2]/ul/li[1]/a').click()

    def input_firstname(self):
        """Make webdriver set random 'First Name' value with presetted length."""
        self.driver.find_element_by_id("input-firstname").send_keys(get_random_name(7))

    def input_lastname(self):
        """Make webdriver set random 'Last Name' value with presetted length."""
        self.driver.find_element_by_id("input-lastname").send_keys(get_random_name(7))

    def input_email(self):
        """
        Make webdriver set random 'E-Mail' value with presetted length of local-name.
        Save generated E-Mail to last_created_email variable (for login).
        """
        self.last_created_email = generate_random_email(5)
        self.driver.find_element_by_id("input-email").send_keys(self.last_created_email)

    def input_telephone(self):
        """Make webdriver set random 'Telephone' value with presetted length."""
        self.driver.find_element_by_id("input-telephone").send_keys(get_random_digit(9))

    def input_password(self):
        """
        Make webdriver set random 'Password' value with presetted length.
        Save generated password to last_created_password variable (for login and confirm).
        """
        self.last_created_password = get_random_password(8)
        self.driver.find_element_by_id("input-password").send_keys(self.last_created_password)

    def input_confirm_password(self):
        """Make webdriver set 'Confirm Password' value (take from last_created_password variable)."""
        self.driver.find_element_by_id("input-confirm").send_keys(self.last_created_password)

    def check_checkbox(self):
        """Make webdriver check 'Privacy Policy' Checkbox."""
        self.driver.find_element_by_name("agree").send_keys(Keys.SPACE)

    def registration(self):
        """Make webdriver click 'Continue' Button for registration complete."""
        self.driver.find_element_by_xpath('//*[@id="content"]/form/div/div/input[2]').click()


# driver = webdriver.Chrome(executable_path=r'../webdrivers/chromedriver.exe')
# base_url = "https://taqc296opencart.000webhostapp.com"
# driver.get(base_url)
#
#
# page = RegistrationPage(driver)
# page.go_to_registration()
# page.input_firstname()
# page.input_lastname()
# page.input_email()
# page.input_telephone()
# page.input_password()
# page.input_confirm_password()
# page.check_checkbox()
# page.registration()

