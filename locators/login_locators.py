
from selenium.webdriver.common.by import By


class LoginLocators:
    EMAIL = (By.XPATH, "//label[normalize-space()='Email']/following-sibling::input")
    PASSWORD = (By.XPATH, "//label[normalize-space()='Jelszó']/following-sibling::input")

    FORGOT_PASSWORD = (By.XPATH, "//a[normalize-space()='Elfelejtetted?']")
    LOGIN_BUTTON = (By.XPATH, "//button[normalize-space()='Belépés']")
    REGISTER_LINK = (By.XPATH, "//a[normalize-space()='Regisztrálj']")
