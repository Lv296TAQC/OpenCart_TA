from driver.driver_factory import DriverFactory
from web_pages.basepage import BasePage


class TestPerformSearch:
    driver = DriverFactory.create_web_driver("chrome")
    driver.find_element()
