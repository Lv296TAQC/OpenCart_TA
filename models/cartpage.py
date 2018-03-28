from selenium import webdriver
from models.driver import MyDriver
from models.loginpage import LoginPage
from models.mainpage import MainPage


class CartPage(MyDriver):

    def go_to_cart(self):
        self.driver.find_element_by_class_name("fa-shopping-cart").click()
        self.driver.refresh()

    def edit_good_qty(self):
        self.driver.find_element_by_class_name("fa-shopping-cart").click()
        self.driver.find_element_by_xpath('//*[@id="content"]/form/div/table/tbody/tr/td[4]/div/input').clear()
        self.driver.find_element_by_xpath('//*[@id="content"]/form/div/table/tbody/tr/td[4]/div/input').send_keys('2')
        self.driver.find_element_by_xpath('//*[@id="content"]/form/div/table/tbody/tr/td[4]/div/span/button[1]').click()

    def delete_good_from_cart(self):
        self.driver.find_element_by_xpath('//*[@id="content"]/form/div/table/tbody/tr/td[4]/div/span/button[2]').click()



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
#
# page = MainPage(driver)
# page.select_mac_product()
# page.add_mac_to_cart()
#
# page = CartPage(driver)
# page.go_to_cart()
# page.edit_good_qty()
# page.delete_good_from_cart()
