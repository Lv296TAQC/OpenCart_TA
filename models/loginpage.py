from selenium import webdriver
from models.driver import MyDriver
from models.registrationpage import RegistrationPage


class LoginPage(MyDriver):

    def go_to_login(self):
        self.driver.find_element_by_xpath('//*[@id="top-links"]/ul/li[2]/a').click()
        self.driver.find_element_by_xpath('//*[@id="top-links"]/ul/li[2]/ul/li[2]/a').click()

    # def input_email(self):
    #     self.driver.driver.find_element_by_id("input-email").send_keys(RegistrationPage.last_created_email)
    def input_email(self):
        self.driver.find_element_by_id("input-email").send_keys('oleksandr.makar.ol@gmail.com')

    # def input_password(self):
    #     self.driver.driver.find_element_by_id("input-password").send_keys(RegistrationPage.last_created_password)
    def input_password(self):
        self.driver.find_element_by_id("input-password").send_keys('saxon123')

    def login(self):
        self.driver.find_element_by_xpath('//*[@id="content"]/div/div[2]/div/form/input').click()



# driver = webdriver.Chrome(executable_path=r'../webdrivers/chromedriver.exe')
# base_url = "https://taqc296opencart.000webhostapp.com"
# driver.get(base_url)

# page = RegistrationPage(driver)
# page.go_to_registration()
# page.input_firstname()
# page.input_lastname()
# page.input_email()
# page.input_telephone()
# page.input_password()
# page.input_confirm_password()
# page.check_checkbox()
# page.registration()
#
# page = LoginPage(driver)
# page.go_to_login()
# page.input_email()
# page.input_password()
# page.login()

