
from pages.registration_page import RegistrationPage


def test_registration_page_opens(driver):
    registration = RegistrationPage(driver)
    registration.open()

    assert "/regisztracio" in driver.current_url
