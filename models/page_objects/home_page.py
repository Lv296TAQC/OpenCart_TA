from models.page_objects.base_page import BasePage


class HomePage(BasePage):
    def to_home_page(self):
        self.driver.get("http://127.0.0.1/")
        return self

    def logging(self):
        self.driver.find_element_by_xpath('//*[@id="top-links"]/ul/li[2]/a').click()
        self.driver.find_element_by_xpath('//*[@id="top-links"]/ul/li[2]/ul/li[2]/a').click()

    def input_email(self):
        self.driver.find_element_by_id('input-email').send_keys('Nick123@gmail.com')

    def input_password(self):
        self.driver.find_element_by_id('input-password').send_keys('123123123')

    def login(self):
        self.driver.find_element_by_xpath('//*[@id="content"]/div/div[2]/div/form/input').click()
