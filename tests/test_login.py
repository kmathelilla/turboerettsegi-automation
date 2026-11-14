
from pages.home_page import HomePage
from pages.login_page import LoginPage


def test_login_with_invalid_credentials(driver):
    home = HomePage(driver)
    home.open()
    home.go_to_login()

    login = LoginPage(driver)

    login.login(
        email="invalid@example.com",
        password="WrongPassword123!"
    )

    assert "/belepes" in driver.current_url
