from selenium.webdriver.common.by import By
from .base import BasePageLocators


class AccountLocators(BasePageLocators):

   ADDRESS_BOOK_LINK = (By.LINK_TEXT, "Address Book")
   EDIT_ACCOUNT_LINK = (By.XPATH, "//div[@id='content']//a[.='Edit Account']")
