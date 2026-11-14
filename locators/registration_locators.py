
from selenium.webdriver.common.by import By


class RegistrationLocators:
    NAME = (
        By.XPATH,
        "//label[normalize-space()='Név']/following-sibling::input"
    )

    EMAIL = (
        By.XPATH,
        "//label[normalize-space()='Email']/following-sibling::input"
    )

    PASSWORD = (
        By.XPATH,
        "//label[normalize-space()='Jelszó']/following-sibling::input"
    )

    SCHOOL = (
        By.XPATH,
        "//input[contains(@placeholder, 'iskolád')]"
    )

    GRADE = (
        By.XPATH,
        "//*[@id='class-grade']"
    )

    GRADE_LIST = (
        By.XPATH,
        "//div[@role='listbox']"
    )

    CLASS = (
        By.XPATH,
        "//button[contains(., 'Jel')]"
    )

    TERMS_CHECKBOX = (
        By.XPATH,
        "//input[@type='checkbox']"
    )

    REGISTER_BUTTON = (
        By.XPATH,
        "//button[normalize-space()='Regisztráció']"
    )

    SUCCESS_MESSAGE = (
        By.XPATH,
        "//p[contains(normalize-space(), 'Elküldtük a megerősítő linket')]"
    )

    @staticmethod
    def school_option(name):
        return (
            By.XPATH,
            f"//*[normalize-space()='{name}']"
        )

    @staticmethod
    def grade_option(grade):
        return (
            By.XPATH,
            f"//div[@role='listbox']//button[normalize-space()='{grade}. évfolyam']"
        )

    @staticmethod
    def class_option(class_name):
        return (
            By.XPATH,
            f"//*[normalize-space()='{class_name}']"
        )
