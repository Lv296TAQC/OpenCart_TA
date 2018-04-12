import allure
import pytest
from elements.formreg import Reg
from faker import Faker


title_error_expect = "Warning: You must agree to the Privacy Policy!"
telephone_error_expect = "Telephone must be between 3 and 32 characters!"
first_name_error_expect = "First Name must be between 1 and 32 characters!"
last_name_error_expect = "Last Name must be between 1 and 32 characters!"
e_mail_error_expect = "E-Mail Address does not appear to be valid!"
password_error_expect = "Password must be between 4 and 20 characters!"
password_confirm_error_expect = "Password confirmation does not match password!"
title_error_cred = "Warning: E-Mail Address is already registered!"
fake = Faker()
first_name = fake.first_name()
last_name = fake.last_name()
email = fake.ascii_safe_email()
telephone = fake.phone_number()
password = 'qwer'
page = Reg()

@pytest.allure.CRITICAL
@allure.step('check if there is an error in the header')
def test_send_none_title():
    page.open()
    page.continue_btn
    assert title_error_expect == page.title_error

@pytest.allure.NORMAL
@allure.step('check if there is an error below the field telephone')
def test_send_none_telephone():
    assert telephone_error_expect == page.telephone_error

@pytest.allure.NORMAL
@allure.step('check if there is an error below the field first name')
def test_send_none_first():
    assert first_name_error_expect == page.first_name_error

@pytest.allure.NORMAL
@allure.step('check if there is an error below the field last name')
def test_send_none_last():
    assert last_name_error_expect == page.last_name_error

@pytest.allure.NORMAL
@allure.step('check if there is an error below the field last email')
def test_send_none_email():
    assert e_mail_error_expect == page.e_mail_error

@pytest.allure.NORMAL
@allure.step('check if there is an error below the field last password')
def test_send_none_password():
    assert password_error_expect == page.password_error
    page.close()

@pytest.allure.NORMAL
@allure.step('checks whether the error  below is all fields')
def test_send_more():
    page.open()
    page.agree_checkbox
    page.first_name = first_name * 10
    page.last_name = last_name * 10
    page.e_mail = email + first_name * 5
    page.telephone = telephone * 10
    page.password = telephone * 10
    page.confirm_password = last_name * 10
    page.continue_btn

@pytest.allure.NORMAL
@allure.step('checks whether the error below is telephone')
def test_send_more_telephone():
    assert telephone_error_expect == page.telephone_error

@pytest.allure.NORMAL
@allure.step('checks whether the error  is below first name')
def test_send_more_first():
    assert first_name_error_expect == page.first_name_error

@pytest.allure.NORMAL
@allure.step('checks whether the error  is below last name')
def test_send_more_last():
    assert last_name_error_expect == page.last_name_error


@pytest.allure.NORMAL
@allure.step('checks whether the error  is below email')
def test_send_more_email():
    assert e_mail_error_expect == page.e_mail_error

@pytest.allure.NORMAL
@allure.step('checks whether the error  is below password')
def test_send_more_password():
    assert password_error_expect == page.password_error

@pytest.allure.NORMAL
@allure.step('checks whether the error  is below confirm password')
def test_send_more_password_confirm():
    assert password_confirm_error_expect == page.password_confirm_error
    page.close()

@pytest.allure.BLOCKER
@allure.step('create account')
def test_send_good():
    page.open()
    page.agree_checkbox
    page.first_name = first_name
    page.last_name = last_name
    page.e_mail = email
    page.telephone = telephone
    page.password = password
    page.confirm_password = password
    page.continue_btn
    assert 'Your Account Has Been Created!' == page.title()
    page.close()

@pytest.allure.BLOCKER
@allure.step('create account with the same cred')
def test_the_same_cred():
    page.open()
    page.agree_checkbox
    page.first_name = first_name
    page.last_name = last_name
    page.e_mail = email
    page.telephone = telephone
    page.password = password
    page.confirm_password = password
    page.continue_btn
    assert title_error_cred == page.title_error
    page.close()

@pytest.allure.BLOCKER
@allure.step('try to be login in')
def test_login():
    page.login()
    page.input_password = password
    page.input_email = email
    page.login_btn
    assert "My Account" == page.title()
    page.close()
