from models.basepage import BasePage


class HomePage(BasePage):

    def go_to_product(self):
        self.driver.get('http://localhost/index.php?route=product/product&product_id=41')
