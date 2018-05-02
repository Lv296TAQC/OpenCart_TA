import pytest

from helpers.constants import Outputs
from helpers.driverfactory import DriverFactory
from helpers.settings import (BASE_HOST,
                              BASE_USER_EMAIL,
                              BASE_USER_PASSWORD)
from pages.home import HomePage


@pytest.fixture(scope="function", autouse="false")
def login_setup(request):
    driver = DriverFactory.get_driver()
    driver.get(BASE_HOST)
    HomePage(driver)\
        .goto_login()\
        .input_password(BASE_USER_PASSWORD)\
        .input_email(BASE_USER_EMAIL)\
        .login()\
        .goto_homepage()
    while Outputs.TEXT_ZERO_PRODUCT_QUANTITY not in HomePage(driver).get_product_quantity():
        HomePage(driver).goto_cart().delete_good_from_cart()
    yield driver

    def logout_teardown():
        while Outputs.TEXT_ZERO_PRODUCT_QUANTITY not in HomePage(driver).get_product_quantity():
            HomePage(driver).goto_cart().delete_good_from_cart()
        HomePage(driver).logout()
        driver.close()

    request.addfinalizer(logout_teardown)
