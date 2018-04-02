import logging
import pytest
from selenium import webdriver
from pages.login import LoginPage
from pages.home import HomePage

driver = webdriver.Chrome()
base_url = 'http://localhost:1234/opencart.com'
driver.get(base_url)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def test_invalid_login_empty_email():
    with pytest.allure.step('Testing invalid login try with empty email'):
        logger.info('Start testing login with invalid email')
        page = HomePage(driver).logging()
        page = LoginPage(driver).input_password().login()
        logger.info('Checking proper work of error handler with invalid email')
        error_text = page.driver.find_element_by_class_name('alert')
        assert 'Warning: No match for E-Mail Address and/or Password' in error_text.text
        logger.info('Work of error handler with invalid email has been checked')


def test_invalid_login_empty_password():
    with pytest.allure.step('Testing invalid login try with empty password'):
        logger.info('Start testing login with invalid password')
        page = HomePage(driver).logging()
        page = LoginPage(driver).input_email().login()
        logger.info('Checking proper work of error handler with invalid password')
        error_text = page.driver.find_element_by_class_name('alert')
        assert 'Warning: No match for E-Mail Address and/or Password' in error_text.text
        logger.info('Work of error handler with invalid password has been checked')


def test_invalid_login_all_empty():
    with pytest.allure.step('Testing invalid login try with empty email and password'):
        logger.info('Start testing login with invalid email and password')
        page = HomePage(driver).logging()
        page = LoginPage(driver).login()
        logger.info('Checking proper work of error handler with invalid email and password')
        error_text = page.driver.find_element_by_class_name('alert')
        assert 'Warning: No match for E-Mail Address and/or Password' in error_text.text
        logger.info('Work of error handler with invalid email and password has been checked')


def test_invalid_login_toomanytries():
    with pytest.allure.step('Testing too much tries to invalid login with empty email and password'):
        logger.info('Start testing too much tries to login with invalid credentials')
        page = HomePage(driver).logging()
        page = LoginPage(driver).login()
        logger.info(
            'Checking proper work of error handler for too much tries to login with invalid credentials')
        error_text = page.driver.find_element_by_class_name('alert')
        assert 'Warning: Your account has exceeded allowed number of login attempts' in error_text.text
        logger.info(
            'Work of error handler for too much tries to login with invalid credentials has been checked')
