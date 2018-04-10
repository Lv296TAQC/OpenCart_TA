import pytest

from helpers.driverfactory import DriverFactory


@pytest.yield_fixture(scope='module')
def init_driver():
    driver = DriverFactory.get_driver()
    driver.maximize_window()
    yield driver
    driver.close()
