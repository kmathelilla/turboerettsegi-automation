
from selenium.webdriver.common.by import By


class HomeLocators:
    LOGIN_BUTTON = (
        By.XPATH,
        "//a[@href='/belepes' and normalize-space()='Belépés']"
    )

    REGISTER_BUTTON = (
        By.XPATH,
        "//a[@href='/belepes' and normalize-space()='Regisztráció']"
    )
