import pytest
from models.personaldetails import PersonalDetails
from pages.home import HomePage
from dbhelpers.customer import DbCustomer
from helpers.settings import BASE_USER_EMAIL, BASE_USER_PASSWORD, BASE_HOST


@pytest.allure.testcase('https://ssu-jira.softserveinc.com/browse/OPENCARTPY-39')
def test_edit_account_info(init_driver):
    new_data = PersonalDetails(first_name="Serhii",
                               last_name="TestLastName",
                               email="taqc296@gmail.com",
                               telephone="12345")
    with pytest.allure.step("Fill 'Edit Account' form with data."):
        driver = init_driver
        driver.get(BASE_HOST)
        HomePage(driver)\
            .goto_login()\
            .input_email(BASE_USER_EMAIL)\
            .input_password(BASE_USER_PASSWORD)\
            .login()\
            .goto_edit_account_page()\
            .fill_edit_account_form(new_data)
    with pytest.allure.step("Compare password from application with password from db."):
        assert new_data == DbCustomer.get_from_db_by_email(new_data)
    HomePage(driver).logout()
