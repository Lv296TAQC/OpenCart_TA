from selenium import webdriver
from models.driver import MyDriver


class LoginPage(MyDriver):

    def go_to_login(self):
        self.driver.find_element_by_xpath('//*[@id="top-links"]/ul/li[2]/a').click()
        self.driver.find_element_by_xpath('//*[@id="top-links"]/ul/li[2]/ul/li[2]/a').click()

    # def input_email(self, email):
    #     self.driver.driver.find_element_by_id("input-email").send_keys(email)
    def input_email(self):
        self.driver.find_element_by_id("input-email").send_keys('oleksandr.makar.ol@gmail.com')

    # def input_password(self, password):
    #     self.driver.driver.find_element_by_id("input-password").send_keys(password)
    def input_password(self):
        self.driver.find_element_by_id("input-password").send_keys('saxon123')

    def login(self):
        self.driver.find_element_by_xpath('//*[@id="content"]/div/div[2]/div/form/input').click()


#
# driver = webdriver.Chrome(executable_path=r'../webdrivers/chromedriver.exe')
# base_url = "https://taqc296opencart.000webhostapp.com"
# driver.get(base_url)
#
# page = LoginPage(driver)
# page.go_to_login()
# page.input_email()
# page.input_password()
# page.login()

