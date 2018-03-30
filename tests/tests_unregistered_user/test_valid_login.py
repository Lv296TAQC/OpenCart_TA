from selenium import webdriver

from pages.login import LoginPage

driver = webdriver.Chrome(executable_path=r'./webdrivers/chromedriver.exe')
base_url = 'https://taqc296opencart.000webhostapp.com'
driver.get(base_url)


def test_00(self):
    LoginPage(self.driver).go_to_login().input_email().input_password().login()
    #  assert page.find_element_by_id("content") in page
