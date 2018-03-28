import pytest
from selenium import webdriver

driver = webdriver.Chrome()


@pytest.fixture(scope='session', autouse=False)
def fixture_for_test(request):
    driver.get("http://127.0.0.1:1234/opencart.com/")

    def fin():
        driver.close()
        #  Need to add if/logout and if/deluser
    request.addfinalizer(fin)
