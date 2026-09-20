from selenium.webdriver.common.by import By
from seleniumpagefactory.Pagefactory import PageFactory

# pip install selenium-page-factory

class TextBoxPage(PageFactory):
    URL = "https://qa-guru.github.io/one-page-form/text-box.html" # Частный случай
    
    def __init__(self, driver):
        self.driver = driver
        self.locators = {
            "full_name_input": ('ID', "userName"),
            "email_input": ('ID', "userEmail"),
            "current_address_input": ('ID', "currentAddress"),
            "permanent_address_input": ('ID', "permanentAddress"),
            "submit_button": ('ID', "submit"),
            "output_box": ('ID', "output"),
            "output_name": ('ID', "name"),
            "output_email": ('ID', "email"),
            "output_current_address": ('CSS', "#output #currentAddress"),
            "output_permnent_address": ('CSS', "#output #permanentAddress")
        }

    def open(self):
        self.driver.get(self.URL)
        return self

    def fill_form(self, name=None, email=None, cur_addr=None, perm_addr=None):
        if name is not None:
            self.full_name_input.set_text(name)
        if email is not None:
            self.email_input.set_text(email)
        if cur_addr is not None:
            self.current_address_input.set_text(cur_addr)
        if perm_addr is not None:
            self.permanent_address_input.set_text(perm_addr)
        return self

    def submit(self):
        self.driver.execute_script("arguments[0].scrollIntoView(true);", self.submit_button)
        self.driver.execute_script("arguments[0].click();", self.submit_button)
        return self

    def get_output_data(self):
        output = self.driver.find_element(By.ID, "output")
        if "has-content" not in (output.get_attribute("class") or ""):
            return None

        name = self.driver.find_element(By.ID, "name").text.replace("Name:", "").strip()
        email = self.driver.find_element(By.ID, "email").text.replace("Email:", "").strip()
        cur_addr = self.driver.find_element(By.CSS_SELECTOR, "#output #currentAddress").text.replace("Current Address :", "").strip()
        perm_addr = self.driver.find_element(By.CSS_SELECTOR, "#output #permanentAddress").text.replace("Permananet Address :", "").strip()
        return {"name": name, "email": email, "cur_addr": cur_addr, "perm_addr": perm_addr}

    def is_email_error_present(self):
        field_class = self.driver.find_element(By.ID, "userEmail").get_attribute("class") or ""
        return "field-error" in field_class or "error" in field_class

    def is_email_valid(self):
        return self.driver.find_element(By.ID, "userEmail").get_property("validity")["valid"]

    def get_name_inner_html(self):
        return self.driver.find_element(By.ID, "name").get_attribute("innerHTML")

