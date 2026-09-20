from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self, driver, base_url):
        self.driver = driver
        self.url = f"{base_url}/login.html"

    LOGIN_INPUT = (By.ID, "login-input")
    PASSWORD_INPUT = (By.ID, "password-input")
    SUBMIT = (By.ID, "submit-button")
    ERROR_MESSAGE = (By.ID, "error-message")
    SUCCESS_PANEL = (By.ID, "success-panel")
    WELCOME = (By.ID, "welcome-message")
    LOGOUT = (By.ID, "logout-button")

    def open(self):
        self.driver.get(self.url)
        self.driver.delete_all_cookies()
        self.driver.execute_script("localStorage.clear();")
        self.driver.get(self.url)
        return self

    def login(self, username="", password=""):
        login_el = self.driver.find_element(*self.LOGIN_INPUT)
        pass_el = self.driver.find_element(*self.PASSWORD_INPUT)
        login_el.clear()
        pass_el.clear()
        if username:
            login_el.send_keys(username)
        if password:
            pass_el.send_keys(password)
        button = self.driver.find_element(*self.SUBMIT)
        self.driver.execute_script("arguments[0].click();", button)
        return self

    def error_text(self):
        return self.driver.find_element(*self.ERROR_MESSAGE).text

    def is_success(self):
        panel = self.driver.find_element(*self.SUCCESS_PANEL)
        return "is-visible" in (panel.get_attribute("class") or "")

    def welcome_text(self):
        return self.driver.find_element(*self.WELCOME).text
