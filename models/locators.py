from selenium.webdriver.common.by import By


class BasePageLocators():
    GO_CART = (By.XPATH, '//*[@id="top-links"]/ul/li[4]/a/i')


class ProductPageLocators(BasePageLocators):
    BTN_CART = (By.ID, 'button-cart')


class CartPageLocators(BasePageLocators):
    GO_CHECKOUT = (By.XPATH, '//*[@id="content"]/div[3]/div[2]/a')


class CheckoutPageLocators(BasePageLocators):
    REGISTER_ACCOUNT = (By.XPATH, '//*[@id="collapse-checkout-option"]/div/div/div[1]/div[1]/label/input')
    GUEST_ACCOUNT = (By.XPATH, '//*[@id="collapse-checkout-option"]/div/div/div[1]/div[2]/label/input')
    STEP_ONE_CONTINUE = (By.ID, 'button-account')
    STEP_TWO_CONTINUE = (By.ID, 'button-register')
    # STEP_TWO_CONTINUE = (By.XPATH, 'button-register')
    # STEP_TWO_CONTINUE = (By.XPATH, 'button-register')
