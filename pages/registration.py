"""
Registration Page Object Model
"""
from selenium.webdriver.common.keys import Keys

from helpers.generators import (generate_random_email,
                                get_random_name,
                                get_random_digit,
                                get_random_password)
from locators.registration import RegistrationPageLocators
from pages.base import BasePage


class RegistrationPage(BasePage):
    """
    Registration Page Object Model
    """
    last_created_password = None
    last_created_email = None

    def input_firstname(self):
        """Make webdriver set random 'First Name' value with presetted length."""
        firstname = self.driver.find_element(*RegistrationPageLocators.FIRSTNAME_INPUT_FIELD)
        firstname.send_keys(get_random_name(7))
        return self

    def input_lastname(self):
        """Make webdriver set random 'Last Name' value with presetted length."""
        lastname = self.driver.find_element(*RegistrationPageLocators.LASTNAME_INPUT_FIELD)
        lastname.send_keys(get_random_name(7))
        return self

    def input_email(self):
        """
        Make webdriver set random 'E-Mail' value with presetted length of local-name.
        Save generated E-Mail to last_created_email variable (for login).
        """
        self.last_created_email = generate_random_email(5)
        email = self.driver.find_element(*RegistrationPageLocators.EMAIL_INPUT_FIELD)
        email.send_keys(self.last_created_email)
        return self

    def input_telephone(self):
        """Make webdriver set random 'Telephone' value with presetted length."""
        telephone = self.driver.find_element(*RegistrationPageLocators.TELEPHONE_INPUT_FIELD)
        telephone.send_keys(get_random_digit(9))
        return self

    def input_password(self):
        """
        Make webdriver set random 'Password' value with presetted length.
        Save generated password to last_created_password variable (for login and confirm).
        """
        self.last_created_password = get_random_password(8)
        password = self.driver.find_element(*RegistrationPageLocators.PASSWORD_INPUT_FIELD)
        password.send_keys(self.last_created_password)
        return self

    def input_confirm_password(self):
        """
        Make webdriver set 'Confirm Password' value
        (take from last_created_password variable).
        """
        confirm_password = self.driver.find_element(
            *RegistrationPageLocators.CONFIRM_PASSWORD_INPUT_FIELD)
        confirm_password.send_keys(self.last_created_password)
        return self

    def check_checkbox(self):
        """Make webdriver check 'Privacy Policy' Checkbox."""
        checkbox = self.driver.find_element(*RegistrationPageLocators.PRIVACY_POLICY_CHECKBOX)
        checkbox.send_keys(Keys.SPACE)
        return self

    def registration(self):
        """Make webdriver click 'Continue' Button for registration complete."""
        registration = self.driver.find_element(*RegistrationPageLocators.CONTINUE_BUTTON)
        registration.click()
        return self
