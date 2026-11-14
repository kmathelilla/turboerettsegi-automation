
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators.registration_locators import RegistrationLocators as R


class RegistrationPage:
    URL = "https://turboerettsegi.hu/regisztracio"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        self.driver.get(self.URL)

    def fill_registration(
        self, name, email, password,
        school, school_option, grade, class_name
    ):
        # Name
        self.wait.until(
            EC.visibility_of_element_located(R.NAME)
        ).send_keys(name)

        # Email
        self.wait.until(
            EC.visibility_of_element_located(R.EMAIL)
        ).send_keys(email)

        # Password
        self.wait.until(
            EC.visibility_of_element_located(R.PASSWORD)
        ).send_keys(password)

        # School autocomplete
        self.wait.until(
            EC.visibility_of_element_located(R.SCHOOL)
        ).send_keys(school)

        self.wait.until(
            EC.element_to_be_clickable(
                R.school_option(school_option)
            )
        ).click()

        # Grade dropdown
        self.wait.until(
            EC.element_to_be_clickable(R.GRADE)
        ).click()

        self.wait.until(
            EC.visibility_of_element_located(R.GRADE_LIST)
        )

        self.wait.until(
            EC.element_to_be_clickable(
                R.grade_option(grade)
            )
        ).click()

        # Class dropdown
        self.wait.until(
            EC.element_to_be_clickable(R.CLASS)
        ).click()

        self.wait.until(
            EC.element_to_be_clickable(
                R.class_option(class_name)
            )
        ).click()

        # Accept terms
        checkbox = self.wait.until(
            EC.element_to_be_clickable(R.TERMS_CHECKBOX)
        )

        if not checkbox.is_selected():
            checkbox.click()

    def get_email_value(self):
        return self.wait.until(
            EC.visibility_of_element_located(R.EMAIL)
        ).get_attribute("value")

    def is_terms_accepted(self):
        return self.wait.until(
            EC.presence_of_element_located(R.TERMS_CHECKBOX)
        ).is_selected()

    def submit_registration(self):
        self.wait.until(
            EC.element_to_be_clickable(R.REGISTER_BUTTON)
        ).click()

    def is_registration_successful(self):
        return self.wait.until(
            EC.visibility_of_element_located(
                R.SUCCESS_MESSAGE
            )
        ).is_displayed()
