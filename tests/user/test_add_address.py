from operator import attrgetter
import pytest
from models.addressbook import AddressBook
from pages.home import HomePage
from pages.addressbook import AddressBookPage
from pages.addaddress import AddAddressPage
from helpers.settings import BASE_USER_EMAIL, BASE_USER_PASSWORD, BASE_HOST


def test_add_correctly_address(init_driver):
    address_data = AddressBook(first_name="edited_firstname",
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
    with pytest.allure.step("Go to Address Book page."):
        HomePage(driver)\
            .goto_login()\
            .input_email(BASE_USER_EMAIL)\
            .input_password(BASE_USER_PASSWORD)\
            .login()\
            .goto_address_book_page()
    with pytest.allure.step("Collect address book list from Address Book page."):
        previous_address_list = AddressBookPage(driver).get_content_info_from_list()
    with pytest.allure.step("Create new address book record."):
        AddressBookPage(driver)\
            .goto_add_address_page()\
            .fill_address_form(address_data)
    with pytest.allure.step("Collect address book list from Address Book page with new record."):
        updated_address_list = AddressBookPage(driver).get_content_info_from_list()
    with pytest.allure.step("Take information from new address record."):
        info_from_new_address = AddressBookPage(driver).get_content_info_from_form(address_data)
    with pytest.allure.step("Append info from new record into old list."):
        previous_address_list.append(info_from_new_address)
    with pytest.allure.step("Retrieving info about successfully added address."):
        assert AddressBookPage(
            driver).get_alert_message_text() == 'Your address has been successfully added'
    with pytest.allure.step("Compare old and new lists."):
        assert sorted(previous_address_list, key=attrgetter(
            'content')) == sorted(updated_address_list, key=attrgetter('content'))
    HomePage(driver).logout()


def test_check_error_messages_in_form(init_driver):
    data = AddressBook(address_1="ad",
                       city="c",
                       post_code="p")
    driver = init_driver
    driver.get(BASE_HOST)
    HomePage(driver)\
        .goto_login()\
        .input_email(BASE_USER_EMAIL)\
        .input_password(BASE_USER_PASSWORD)\
        .login()\
        .goto_address_book_page()\
        .goto_add_address_page()\
        .fill_address_form(data)
    with pytest.allure.step("Check error message in the 'First Name' field."):
        assert AddAddressPage(
            driver).get_first_name_error() == "First Name must be between 1 and 32 characters!"
    with pytest.allure.step("Check error message in the 'Last Name' field."):
        assert AddAddressPage(
            driver).get_last_name_error() == "Last Name must be between 1 and 32 characters!"
    with pytest.allure.step("Check error message in the 'Address 1' field."):
        assert AddAddressPage(
            driver).get_address1_error() == "Address must be between 3 and 128 characters!"
    with pytest.allure.step("Check error message in the 'City' field."):
        assert AddAddressPage(
            driver).get_city_error() == "City must be between 2 and 128 characters!"
    with pytest.allure.step("Check error message in the 'Post Code' field."):
        assert AddAddressPage(
            driver).get_postcode_error() == "Postcode must be between 2 and 10 characters!"
    with pytest.allure.step("Check error message in the 'Country' drop down option."):
        assert AddAddressPage(
            driver).get_region_error() == "Please select a region / state!"
    HomePage(driver).logout()
