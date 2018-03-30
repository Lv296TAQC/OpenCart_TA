import pytest
from selenium import webdriver

# @pytest.fixture(scope="session", autouse=True)
# def conf_fixture(request):
#     driver = webdriver.Chrome()
#     def auto_session_teardown():
#         driver.close()
#     request.addfinalizer(auto_session_teardown)
