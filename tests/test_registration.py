import time

from data.registration_data import REGISTRATION_DATA
from pages.registration_page import RegistrationPage


def test_registration_form(driver):
    registration = RegistrationPage(driver)
    registration.open()

    registration.fill_registration(**REGISTRATION_DATA)

    assert (
        registration.get_email_value()
        == REGISTRATION_DATA["email"]
    )

    assert registration.is_terms_accepted()

    registration.submit_registration()
    #time.sleep(15)