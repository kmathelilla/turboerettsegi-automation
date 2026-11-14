
from selenium.webdriver.common.by import By

from pages.home_page import HomePage
from pages.registration_page import RegistrationPage


def test_registration_form(driver):
    home = HomePage(driver)
    home.open()
    home.go_to_registration()

    registration = RegistrationPage(driver)

    registration.fill_registration(
        name="Test User",
        email="test@example.com",
        password="TestPassword123!"
    )

    email_field = driver.find_element(
        By.XPATH,
        "//label[normalize-space()='Email']/following-sibling::input"
    )

    assert email_field.get_attribute("value") == "test@example.com"
