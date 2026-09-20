from selenium.webdriver.common.by import By


class TextBoxPage:
    def __init__(self, driver, base_url):
        self.driver = driver
        self.url = f"{base_url}/text-box.html"

    FULL_NAME = (By.ID, "userName")
    EMAIL = (By.ID, "userEmail")
    CURRENT_ADDRESS = (By.ID, "currentAddress")
    PERMANENT_ADDRESS = (By.ID, "permanentAddress")
    SUBMIT = (By.ID, "submit")
    OUTPUT = (By.ID, "output")
    OUT_NAME = (By.ID, "name")
    OUT_EMAIL = (By.ID, "email")
    OUT_CUR = (By.CSS_SELECTOR, "#output #currentAddress")
    OUT_PERM = (By.CSS_SELECTOR, "#output #permanentAddress")

    def open(self):
        self.driver.get(self.url)
        return self

    def fill_name(self, value):
        el = self.driver.find_element(*self.FULL_NAME)
        el.clear()
        el.send_keys(value)
        return self

    def fill_email(self, value):
        el = self.driver.find_element(*self.EMAIL)
        el.clear()
        el.send_keys(value)
        return self

    def fill_current_address(self, value):
        el = self.driver.find_element(*self.CURRENT_ADDRESS)
        el.clear()
        el.send_keys(value)
        return self

    def fill_permanent_address(self, value):
        el = self.driver.find_element(*self.PERMANENT_ADDRESS)
        el.clear()
        el.send_keys(value)
        return self

    def fill_form(self, name=None, email=None, cur_addr=None, perm_addr=None):
        if name is not None:
            self.fill_name(name)
        if email is not None:
            self.fill_email(email)
        if cur_addr is not None:
            self.fill_current_address(cur_addr)
        if perm_addr is not None:
            self.fill_permanent_address(perm_addr)
        return self

    def submit(self):
        btn = self.driver.find_element(*self.SUBMIT)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", btn)
        self.driver.execute_script("arguments[0].click();", btn)
        return self

    def get_output(self):
        output = self.driver.find_element(*self.OUTPUT)
        if "has-content" not in (output.get_attribute("class") or ""):
            return None
        return {
            "Name": self.driver.find_element(*self.OUT_NAME).text.replace("Name:", "").strip(),
            "Email": self.driver.find_element(*self.OUT_EMAIL).text.replace("Email:", "").strip(),
            "Current Address": self.driver.find_element(*self.OUT_CUR)
            .text.replace("Current Address :", "")
            .strip(),
            "Permananet Address": self.driver.find_element(*self.OUT_PERM)
            .text.replace("Permananet Address :", "")
            .strip(),
        }

    def is_result_hidden(self):
        return self.get_output() is None

    def is_email_valid(self):
        return self.driver.find_element(*self.EMAIL).get_property("validity")["valid"]
