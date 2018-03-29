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


def test_valid_login():
    with pytest.allure.step('Testing proper login function'):
        logger.info('Start testing login with valid credentials function')
        page = HomePage(driver).logging()
        page = LoginPage(driver).input_email().input_password().login()
        logger.info('Checking proper work of login function')
        assert page.driver.title == 'My Account'
        logger.info('Work of login function has been checked')
