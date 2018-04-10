from elements.formreg import Reg


def test_send():
    page = Reg()
    page.open()
    page.first_name = 'fakename'
    page.last_name = 'fakefree_email_domain'
    page.agri_checkbox
    page.continue_btn
