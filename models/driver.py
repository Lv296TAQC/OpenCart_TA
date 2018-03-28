from selenium import webdriver


class MyDriver:
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=r'../webdrivers/chromedriver.exe')
        self.base_url = "https://taqc296opencart.000webhostapp.com"

    # def title(self):
    #     return self.driver.title

    def go_to_home(self):
        self.driver.get(self.base_url)
        # self.driver.Url = Driver.base_url + url

    # def close(self):
    #     self.driver.close()
