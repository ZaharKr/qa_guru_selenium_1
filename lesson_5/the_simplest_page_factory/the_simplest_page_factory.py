from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from seleniumpagefactory.Pagefactory import PageFactory


class LoginPage(PageFactory):
    def __init__(self, driver):
        self.driver = driver
        self.locators = {
            "username_input": ("ID", "login-input"),
            "password_input": ("ID", "password-input"),
            "submit_button": ("ID", "submit-button"),
            "error_message": ("ID", "error-message"),
            "welcome_message": ("ID", "welcome-message"),
        }

    def open(self):
        self.driver.get("https://qa-guru.github.io/one-page-form/login.html")
        self.driver.execute_script("localStorage.clear();")
        self.driver.get("https://qa-guru.github.io/one-page-form/login.html")
        return self

    def login(self, user, password):
        self.username_input.set_text(user)
        self.password_input.set_text(password)
        self.driver.execute_script("arguments[0].click();", self.submit_button)
        return self


if __name__ == "__main__":
    opts = Options()
    opts.add_argument("--headless=new")
    driver = webdriver.Chrome(options=opts)
    try:
        page = LoginPage(driver).open()
        page.login("user1", "badpass")
        assert "Wrong login or password" in page.error_message.get_text()

        page.open().login("user1", "password1")
        assert "user1" in page.welcome_message.get_text()
        print("OK: page factory login")
    finally:
        driver.quit()
