from OpenCart_TA.models.locators import ShoppingCartLocators
from OpenCart_TA.models.page_objects.home_page import HomePage


class EmptyShoppingCart(HomePage):
    # url = "http://127.0.0.1/opencart.com/index.php?route=checkout/cart"

    def is_on_cart_page(self):
        if self.driver.current_url == "http://127.0.0.1/opencart.com/index.php?route=checkout/cart":
            print(True)
            return True
        print(False)
        return False

    def is_cart_empty(self):
        empty_cart_text = self.driver.find_element(*ShoppingCartLocators.EMPTY_CART_TEXT)
        if empty_cart_text:
            print("Yout cart is empty!")
            return True

    def click_on_continue_button(self):
        continue_button = self.driver.find_element(*ShoppingCartLocators.CONTINUE_BUTTON)
        continue_button.click()
