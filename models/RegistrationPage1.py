import pytest
from tests.tests_registered_user.conftest import driver


@pytest.mark.usefixtures("fixture_for_test")
class RegistrationPage:
    def goto(self):
        driver.find_element_by_xpath('//*[@id="top-links"]/ul/li[2]/a').click()
        driver.find_element_by_xpath('//*[@id="top-links"]/ul/li[2]/ul/li[1]/a').click()
