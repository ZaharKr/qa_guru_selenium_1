from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self, driver, base_url):
        self.driver = driver
        self.url = f"{base_url}/login.html"

    LOGIN = (By.ID, "login-input")
    PASSWORD = (By.ID, "password-input")
    SUBMIT = (By.ID, "submit-button")
    ERROR = (By.ID, "error-message")
    SUCCESS = (By.ID, "success-panel")
    WELCOME = (By.ID, "welcome-message")

    def open(self):
        self.driver.get(self.url)
        self.driver.delete_all_cookies()
        self.driver.execute_script("localStorage.clear();")
        self.driver.get(self.url)
        return self

    def fill_login(self, value):
        el = self.driver.find_element(*self.LOGIN)
        el.clear()
        if value:
            el.send_keys(value)
        return self

    def fill_password(self, value):
        el = self.driver.find_element(*self.PASSWORD)
        el.clear()
        if value:
            el.send_keys(value)
        return self

    def click_login(self):
        btn = self.driver.find_element(*self.SUBMIT)
        self.driver.execute_script("arguments[0].click();", btn)
        return self

    def login(self, username="", password=""):
        return self.fill_login(username).fill_password(password).click_login()

    def error_text(self):
        return self.driver.find_element(*self.ERROR).text

    def is_success(self):
        panel = self.driver.find_element(*self.SUCCESS)
        return "is-visible" in (panel.get_attribute("class") or "")

    def welcome_text(self):
        return self.driver.find_element(*self.WELCOME).text
