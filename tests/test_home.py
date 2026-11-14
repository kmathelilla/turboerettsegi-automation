
from pages.home_page import HomePage


def test_navigate_to_login(driver):
    home = HomePage(driver)
    home.open()
    home.go_to_login()

    assert "/belepes" in driver.current_url


def test_navigate_to_registration(driver):
    home = HomePage(driver)
    home.open()
    home.go_to_registration()

    assert "/belepes" in driver.current_url
