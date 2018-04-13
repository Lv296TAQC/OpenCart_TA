import pytest
from models.addressbook import AddressBook
from pages.home import HomePage
from pages.addressbook import AddressBookPage
from helpers.settings import BASE_USER_EMAIL, BASE_USER_PASSWORD, BASE_HOST


@pytest.allure.testcase('https://ssu-jira.softserveinc.com/browse/OPENCARTPY-42')
def test_delete_address_by_index(init_driver, index=2):
    address = AddressBook(first_name="edited_firstname",
                          last_name="edited_lastname",
                          company="edited_company",
                          address_1="edited_address1",
                          address_2="edited_address2",
                          city="edited_city",
                          post_code="e_postcode",
                          country="Ukraine",
                          region_state="Ternopil's'ka Oblast'")
    driver = init_driver
    driver.get(BASE_HOST)
    HomePage(driver)\
        .goto_login()\
        .input_email(BASE_USER_EMAIL)\
        .input_password(BASE_USER_PASSWORD)\
        .login()\
        .goto_address_book_page()
    while AddressBookPage(driver).records_count() < index + 1:
        AddressBookPage(driver)\
            .goto_add_address_page()\
            .fill_address_form(address)
    with pytest.allure.step("Take the number of address book records on the page."):
        previous_address_list = AddressBookPage(driver).records_count()
    with pytest.allure.step("Delete address book record by index %d." % index):
        AddressBookPage(driver).delete_record_by_index(index)
    with pytest.allure.step("Take len of address list after deleting the record"):
        updated_address_list = AddressBookPage(driver).records_count()
    with pytest.allure.step("Compare the length of the list before and after deleting the record"):
        assert previous_address_list - 1 == updated_address_list
    HomePage(driver).logout()
