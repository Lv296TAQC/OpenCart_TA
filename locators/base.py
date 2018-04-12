"""
All common locators for all Pages are placed here
"""
from selenium.webdriver.common.by import By

from helpers.settings import BASE_HOST


# pylint: disable=too-few-public-methods
class BasePageLocators:
    """
    All common locators for all Pages are placed here
    """
    GO_CART = (By.XPATH, '//*[@id="top-links"]/ul/li[4]/a/i')
    MY_ACCOUNT_DROPDOWN = (By.XPATH, '//*[@id="top-links"]/ul/li[2]/a')
    GO_LOGIN = (By.XPATH, '//*[@id="top-links"]/ul/li[2]/ul/li[2]/a')
    DESKTOPS = (By.XPATH, '//a[text()="Desktops"]')
    LAPTOPS = (By.XPATH, '//a[text()="Laptops & Notebooks"]')
    TABLETS = (By.XPATH, '//a[text()="Tablets"]')
    SOFTWARE = (By.XPATH, '//a[text()="Software"]')
    PHONES = (By.XPATH, '//a[text()="Phones & PDAs"]')
    CAMERAS = (By.XPATH, '//a[text()="Cameras"]')
    MP3S = (By.XPATH, '//a[text()="MP3 Players"]')
    BTN_GREY_CART = (By.ID, "cart")
    EMPTY_CART_BUTTON_TEXT = (By.XPATH, '//p[text()="Your shopping cart is empty!"]')
    BTN_GREY_CARD_AMOUNT = (By.ID, "cart-total")
    LINK_VIEW_CART = (By.XPATH, '//*[@id="cart"]/ul/li[2]/div/p/a[1]')
    LINK_CHECKOUT = (By.XPATH, '//*[@id="cart"]/ul/li[2]/div/p/a[2]')
    BTN_DELETE = (By.XPATH, '//*[@id="cart"]/ul/li[1]/table/tbody/tr[1]/td[5]/button')
    COMPONENTS = (By.XPATH, '//a[text()="Components"]')
    MONITORS = (By.XPATH, '//a[contains(text(),"Monitors")]')
    MAC = (By.XPATH, '//a[contains(text(),"Mac")]')
    ALLDESKTOPS = (By.XPATH, '//a[contains(text(),"Show All Desktops")]')
    MACS = (By.XPATH, '//a[contains(text(),"Macs")]')
    WINDOWS = (By.XPATH, '//a[contains(text(),"Windows")]')
    ALLLEPTOPS = (By.XPATH, '//a[contains(text(),"Show All Laptops & Notebooks")]')
    MICE = (By.XPATH, '//a[contains(text(),"Mice and Trackballs")]')
    PRINTERS = (By.XPATH, '//a[contains(text(),"Printers")]')
    SCANNERS = (By.XPATH, '//a[contains(text(),"Scanners")]')
    WEBCAMERAS = (By.XPATH, '//a[contains(text(),"Web Cameras")]')
    ALLCOMPONENTS = (By.XPATH, '//a[contains(text(),"Show All Components")]')
    LIST_DESKTOPS = (By.XPATH, '//*[@id="menu"]/div[2]/ul/li[1]/div/div/ul/li/a')
    LIST_LAPTOPS = (By.XPATH, '//*[@id="menu"]/div[2]/ul/li[2]/div/div/ul/li/a')
    LIST_COMPONENS = (By.XPATH, '//*[@id="menu"]/div[2]/ul/li[3]/div/div/ul/li/a')
    LOGOUT = (By.XPATH, "//ul[@class='list-inline']//a[.='Logout']")
    PC = (By.XPATH, '//a[contains(text(),"PC")]')

    # FOOTER
    RETURNS = (By.CSS_SELECTOR, f'a[href="{BASE_HOST}/index.php?route=account/return/add"]')
