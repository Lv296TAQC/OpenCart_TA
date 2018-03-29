# import pytest
#
# from helpers.driverfactory import DriverFactory
# from webpages.searchpage import SearchPage
#
#
# @pytest.yield_fixture(scope="class")
# def initialize(request):
#     driver = DriverFactory.create_web_driver("chrome")
#     driver.maximize_window()
#     driver.get("https://taqc296opencart.000webhostapp.com/")
#     driver.get('https://taqc296opencart.000webhostapp.com/index.php?route=product/search')
#     searchpage = SearchPage(driver)
#     request.cls.searchpage = searchpage
#
#     yield
#
#     driver.close()
