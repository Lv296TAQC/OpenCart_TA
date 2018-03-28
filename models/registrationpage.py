from selenium import webdriver
from models.driver import MyDriver


class RegistrationPage(MyDriver):

    def go_to_registration(self):
        self.driver.driver.find_element_by_xpath('//*[@id="top-links"]/ul/li[2]/a').click()
        self.driver.driver.find_element_by_xpath('//*[@id="top-links"]/ul/li[2]/ul/li[1]/a').click()

    def input_firstname(self, firstname):
        self.driver.driver.find_element_by_id("input-firstname").send_keys(firstname)

    def input_lastname(self, lastname):
        self.driver.driver.find_element_by_id("input-lastname").send_keys(lastname)

    def input_email(self, email):
        self.driver.driver.find_element_by_id("input-email").send_keys(email)

    def input_telephone(self, telephone):
        self.driver.driver.find_element_by_id("input-telephone").send_keys(telephone)

    def input_password(self, password):
        self.driver.driver.find_element_by_id("input-password").send_keys(password)

    def input_confirm_password(self, confirm_password):
        self.driver.driver.find_element_by_id("input-confirm").send_keys(confirm_password)

    def check_checkbox(self):
        self.driver.driver.find_element_by_name("agree").click()

    def registration(self):
        self.driver.driver.find_element_by_xpath('//*[@id="content"]/form/div/div/input[2]').click()

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
