from models.driver import MyDriver


class LoginPage:
    driver = MyDriver()

    def go_to_login(self):  # this sh*t shouldn't be here. It should be in driver
        self.driver.go_to_home()
        self.driver.driver.find_element_by_xpath('//*[@id="top-links"]/ul/li[2]/a').click()
        self.driver.driver.find_element_by_xpath('//*[@id="top-links"]/ul/li[2]/ul/li[2]/a').click()

    # def input_email(self, email):
    #     self.driver.driver.find_element_by_id("input-email").send_keys(email)
    def input_email(self):
        self.driver.driver.find_element_by_id("input-email").send_keys('oleksandr.makar.ol@gmail.com')

    # def input_password(self, password):
    #     self.driver.driver.find_element_by_id("input-password").send_keys(password)
    def input_password(self):
        self.driver.driver.find_element_by_id("input-password").send_keys('saxon123')

    def login(self):
        self.driver.driver.find_element_by_xpath('//*[@id="content"]/div/div[2]/div/form/input').click()


page = LoginPage()
page.go_to_login()
page.input_email()
page.input_password()
page.login()
