from models.personaldetails import PersonalDetails
from db.customer import Customer


def test_edit_user_info(conf):
    info = PersonalDetails(first_name="Serhii",
                           last_name="TestLastName",
                           email="taqc296@gmail.com",
                           telephone="12345")
    conf.personal_details.edit(info)
    assert info == Customer.get_from_db_by_email(info)
