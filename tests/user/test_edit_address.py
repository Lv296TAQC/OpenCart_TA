import pytest
from models.addressbook import AddressBook
from pages.home import HomePage
from pages.addressbook import AddressBookPage
from helpers.settings import BASE_USER_EMAIL, BASE_USER_PASSWORD, BASE_HOST


def test_edit_address_by_index(init_driver, index=3):
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
        .goto_addressbook_page()
    while AddressBookPage(driver).records_count() < index + 1:
        AddressBookPage(driver)\
            .goto_addaddres_page()\
            .fill_address_form(address)
    AddressBookPage(driver).\
        goto_editaddress_page_by_index(index).\
        fill_address_form(address)
    with pytest.allure.step("Take information from edited address record from Add Address form."):
        info_from_edited_address = AddressBookPage.get_content_info_from_form(address)
    with pytest.allure.step("Take information about edited address on Address Book page."):
        updated_info_from_address_list = AddressBookPage(driver).get_content_info_by_index(index)
    with pytest.allure.step("Retrieving info about successfully updated address."):
        assert AddressBookPage(
            driver).get_alert_message_text() == 'Your address has been successfully updated'
    with pytest.allure.step("Compare info about edited address."):
        assert info_from_edited_address == updated_info_from_address_list
    HomePage(driver).logout()
