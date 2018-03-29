from helpers.driver_factory import DriverFactory


class TestPerformSearch:
    driver = DriverFactory.create_web_driver("chrome")
    driver.find_element()
