
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators.home_locators import HomeLocators as H


class HomePage:
    URL = "https://turboerettsegi.hu/"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        self.driver.get(self.URL)

    def go_to_login(self):
        self.wait.until(
            EC.element_to_be_clickable(H.LOGIN_BUTTON)
        ).click()

    def go_to_registration(self):
        self.wait.until(
            EC.element_to_be_clickable(H.REGISTER_BUTTON)
        ).click()
