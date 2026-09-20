import time

from selenium.webdriver.common.by import By

from chrome_setup import PAUSE, TEXT_BOX_URL, click_submit, create_driver

USER_NAME = (By.ID, "userName")
USER_EMAIL = (By.ID, "userEmail")
CURRENT_ADDRESS = (By.ID, "currentAddress")
PERMANENT_ADDRESS = (By.ID, "permanentAddress")
OUTPUT = (By.ID, "output")


class TextBoxTests:
    def __init__(self, url, driver):
        self.url = url
        self.driver = driver

    def open(self):
        self.driver.get(self.url)
        time.sleep(PAUSE)

    def fill(self, name="", email="", current="", permanent=""):
        if name:
            self.driver.find_element(*USER_NAME).send_keys(name)
        if email:
            self.driver.find_element(*USER_EMAIL).send_keys(email)
        if current:
            self.driver.find_element(*CURRENT_ADDRESS).send_keys(current)
        if permanent:
            self.driver.find_element(*PERMANENT_ADDRESS).send_keys(permanent)
        click_submit(self.driver)
        time.sleep(PAUSE)

    def test_all_fields(self):
        self.open()
        name = "Иван Иванов"
        email = "ivan@example.com"
        current = "Москва, Тверская 1"
        permanent = "СПб, Невский 10"
        self.fill(name, email, current, permanent)
        result = self.driver.find_element(*OUTPUT).text
        assert name in result
        assert email in result
        assert current in result
        assert permanent in result
        print("OK: all fields")

    def test_name_and_email(self):
        self.open()
        self.fill(name="Пётр Петров", email="petr@mail.ru")
        result = self.driver.find_element(*OUTPUT).text
        assert "Пётр Петров" in result
        assert "petr@mail.ru" in result
        print("OK: name and email")


if __name__ == "__main__":
    driver = create_driver()
    try:
        suite = TextBoxTests(TEXT_BOX_URL, driver)
        suite.test_all_fields()
        suite.test_name_and_email()
    finally:
        driver.quit()
