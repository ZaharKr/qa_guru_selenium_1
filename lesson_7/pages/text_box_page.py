from selenium.webdriver.common.by import By


class TextBoxPage:
    def __init__(self, driver, base_url):
        self.driver = driver
        self.url = f"{base_url}/text-box.html"

    FULL_NAME = (By.ID, "userName")
    EMAIL = (By.ID, "userEmail")
    CURRENT_ADDRESS = (By.ID, "currentAddress")
    PERMANENT_ADDRESS = (By.ID, "permanentAddress")
    SUBMIT_BUTTON = (By.ID, "submit")
    OUTPUT_BOX = (By.ID, "output")
    OUTPUT_NAME = (By.ID, "name")
    OUTPUT_EMAIL = (By.ID, "email")
    OUTPUT_CUR_ADDR = (By.CSS_SELECTOR, "#output #currentAddress")
    OUTPUT_PERM_ADDR = (By.CSS_SELECTOR, "#output #permanentAddress")

    def open(self):
        self.driver.get(self.url)
        return self

    def fill_form(self, name=None, email=None, cur_addr=None, perm_addr=None):
        if name is not None:
            field = self.driver.find_element(*self.FULL_NAME)
            field.clear()
            field.send_keys(name)
        if email is not None:
            self.driver.find_element(*self.EMAIL).send_keys(email)
        if cur_addr is not None:
            self.driver.find_element(*self.CURRENT_ADDRESS).send_keys(cur_addr)
        if perm_addr is not None:
            self.driver.find_element(*self.PERMANENT_ADDRESS).send_keys(perm_addr)
        return self

    def submit(self):
        button = self.driver.find_element(*self.SUBMIT_BUTTON)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", button)
        self.driver.execute_script("arguments[0].click();", button)
        return self

    def get_output_data(self):
        output = self.driver.find_element(*self.OUTPUT_BOX)
        if "has-content" not in (output.get_attribute("class") or ""):
            return None
        return {
            "name": self.driver.find_element(*self.OUTPUT_NAME).text.replace("Name:", "").strip(),
            "email": self.driver.find_element(*self.OUTPUT_EMAIL).text.replace("Email:", "").strip(),
            "cur_addr": self.driver.find_element(*self.OUTPUT_CUR_ADDR)
            .text.replace("Current Address :", "")
            .strip(),
            "perm_addr": self.driver.find_element(*self.OUTPUT_PERM_ADDR)
            .text.replace("Permananet Address :", "")
            .strip(),
        }

    def is_email_valid(self):
        return self.driver.find_element(*self.EMAIL).get_property("validity")["valid"]
