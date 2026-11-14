
from selenium.webdriver.common.by import By


class RegistrationLocators:
    NAME = (By.XPATH, "//label[normalize-space()='Név']/following-sibling::input")
    EMAIL = (By.XPATH, "//label[normalize-space()='Email']/following-sibling::input")
    PASSWORD = (By.XPATH, "//label[normalize-space()='Jelszó']/following-sibling::input")

    SCHOOL = (By.XPATH, "//input[contains(@placeholder, 'iskolád')]")
    SCHOOL_OPTION = (
        By.XPATH,
        "//*[normalize-space()='Salgótarjáni Madách Imre Gimnázium']"
    )

    GRADE = (By.XPATH, "//button[contains(., 'Évfolyam')]")
    CLASS = (By.XPATH, "//button[contains(., 'Jel')]")

    TERMS_CHECKBOX = (By.XPATH, "//input[@type='checkbox']")

    REGISTER_BUTTON = (By.XPATH, "//button[normalize-space()='Regisztráció']")
