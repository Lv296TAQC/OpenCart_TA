from selenium import webdriver
from models.driver import MyDriver
from models.loginpage import LoginPage


class MainPage(MyDriver):

    def select_mac_product(self):
        self.driver.find_element_by_xpath('//*[@id="menu"]/div[2]/ul/li[1]/a').click()
        self.driver.find_element_by_xpath('//*[@id="menu"]/div[2]/ul/li[1]/div/div/ul/li[2]/a').click()

    def add_mac_to_cart(self):
        self.driver.find_element_by_xpath('//*[@id="content"]/div[2]/div/div/div[1]/a/img').click()
        self.driver.find_element_by_id("button-cart").click()

# driver = webdriver.Chrome(executable_path=r'../webdrivers/chromedriver.exe')
# base_url = "https://taqc296opencart.000webhostapp.com"
# driver.get(base_url)
#
# page = LoginPage(driver)
# page.go_to_login()
# page.input_email()
# page.input_password()
# page.login()
#
# page = MainPage(driver)
# page.select_mac_product()
# page.add_mac_to_cart()
