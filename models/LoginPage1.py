from models.driver import Driver


class LoginPage:
    @staticmethod
    def goto():
        Driver.driver.find_element_by_xpath('//*[@id="top-links"]/ul/li[2]/a').click()
        Driver.driver.find_element_by_xpath('//*[@id="top-links"]/ul/li[2]/ul/li[2]/a').click()

    @staticmethod
    def login():
        email = Driver.driver.find_element_by_id("input-email")
        email.send_keys("good_email_from_generator")
        password = Driver.driver.find_element_by_id("input-password")
        password.send_keys("good_password_from_generator")
        Driver.driver.find_element_by_xpath('//*[@id="content"]/div/div[2]/div/form/input').click()  # may bee Return
