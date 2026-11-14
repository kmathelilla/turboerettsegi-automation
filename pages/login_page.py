
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage:
    URL = "https://turboerettsegi.hu/"

    LOGIN_BUTTON = (By.XPATH, "//a[@href='/belepes' and normalize-space()='Belépés']")
    REGISTER_BUTTON = (By.XPATH, "//a[@href='/belepes' and normalize-space()='Regisztráció']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        self.driver.get(self.URL)

    def go_to_login(self):
        self.wait.until(
            EC.element_to_be_clickable(self.LOGIN_BUTTON)
        ).click()

    def go_to_registration(self):
        self.wait.until(
            EC.element_to_be_clickable(self.REGISTER_BUTTON)
        ).click()
