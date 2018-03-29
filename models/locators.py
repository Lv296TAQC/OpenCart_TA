from selenium.webdriver.common.by import By


class HomePageLocators:
    COMPONENTS_TAB = (By.XPATH,'//*[@id="menu"]/div[2]/ul/li[3]/a')
    SHOPPING_CART_TAB = (By.XPATH, '//*[@id="top-links"]/ul/li[4]/a')
    MONITORS = (By.XPATH, '//*[@id="menu"]/div[2]/ul/li[3]/div/div/ul/li[2]/a')
    PHONES = (By.XPATH, '//*[@id="menu"]/div[2]/ul/li[6]/a')

class ShoppingCartLocators:
    EMPTY_CART_TEXT = (By.XPATH, '//*[@id="content"]/p')
    CONTINUE_BUTTON = (By.XPATH, '//*[@id="content"]/div/div/a')

class SearchProductLocators(HomePageLocators):
    ADD_APPLE_CINEMA = (By.XPATH, '//*[@id="content"]/div[3]/div[1]/div/div[2]/div[2]/button[1]')