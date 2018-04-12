import pytest
from models.password import Password
from pages.home import HomePage
from pages.account import AccountPage
from pages.password import PasswordPage
from dbhelpers.customer import DbCustomer
from helpers.settings import BASE_USER_EMAIL, BASE_USER_PASSWORD, BASE_HOST


def test_compare_changed_password(init_driver):
    user_password = Password(password='root')
    driver = init_driver
    driver.get(BASE_HOST)
    with pytest.allure.step("Change password on Password page."):
        HomePage(driver)\
            .goto_login()\
            .input_email(BASE_USER_EMAIL)\
            .input_password(BASE_USER_PASSWORD)\
            .login()\
            .goto_password_page()\
            .fill_password_form(user_password)
    with pytest.allure.step("Retrieving info about successfully updated password."):
        assert (AccountPage(driver).get_account_alert_message_text() ==
                'Success: Your password has been successfully updated.')
    with pytest.allure.step("Take text data from E-Mail field."):
        email_from_form = AccountPage(driver)\
            .goto_edit_account_page()\
            .get_email_from_form()
    with pytest.allure.step("Take salt from db table oc_customer."):
        salt_from_db = DbCustomer.get_salt_by_email(email_from_form)
    with pytest.allure.step("Encrypt password."):
        encrypted_pass = PasswordPage\
            .encrypt_user_password(password=user_password, salt=salt_from_db)
    with pytest.allure.step("Take password from db table oc_customer."):
        password_from_db = DbCustomer.get_password_by_email(email_from_form)
    with pytest.allure.step("Compare password from UI with password from DB."):
        assert encrypted_pass == password_from_db
    HomePage(driver).logout()
