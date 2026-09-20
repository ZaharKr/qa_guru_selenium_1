from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait


class RegistrationPage:
    def __init__(self, driver, base_url):
        self.driver = driver
        self.url = f"{base_url}/automation-practice-form.html"
        self.wait = WebDriverWait(driver, 10)

    FIRST_NAME = (By.ID, "firstName")
    LAST_NAME = (By.ID, "lastName")
    EMAIL = (By.ID, "userEmail")
    PHONE = (By.ID, "userNumber")
    DOB = (By.ID, "dateOfBirthInput")
    YEAR = (By.CSS_SELECTOR, ".react-datepicker__year-select")
    MONTH = (By.CSS_SELECTOR, ".react-datepicker__month-select")
    SUBJECTS = (By.ID, "subjectsInput")
    UPLOAD = (By.ID, "uploadPicture")
    ADDRESS = (By.ID, "currentAddress")
    STATE = (By.ID, "state")
    CITY = (By.ID, "city")
    SUBMIT = (By.ID, "submit")
    RESULT = (By.ID, "resultModal")

    def open(self):
        self.driver.get(self.url)
        return self

    def _close_overlays(self):
        self.driver.execute_script(
            "const b=document.getElementById('fixedban'); if(b) b.remove();"
            "const f=document.getElementsByTagName('footer')[0]; if(f) f.style.display='none';"
        )
        return self

    def set_firstname(self, value):
        self.driver.find_element(*self.FIRST_NAME).send_keys(value)
        return self

    def set_lastname(self, value):
        self.driver.find_element(*self.LAST_NAME).send_keys(value)
        return self

    def set_email(self, value):
        self.driver.find_element(*self.EMAIL).send_keys(value)
        return self

    def set_gender(self, value):
        label = self.driver.find_element(
            By.XPATH, f"//div[@id='genterWrapper']//label[.//input[@value='{value}']]"
        )
        self.driver.execute_script("arguments[0].click();", label)
        return self

    def set_phone(self, value):
        self.driver.find_element(*self.PHONE).send_keys(value)
        return self

    def set_birthdate(self, year, month, day):
        self._close_overlays()
        self.driver.find_element(*self.DOB).click()
        Select(self.driver.find_element(*self.YEAR)).select_by_value(year)
        Select(self.driver.find_element(*self.MONTH)).select_by_value(month)
        day_css = (
            f".react-datepicker__day--{int(day):03d}"
            f":not(.react-datepicker__day--outside-month)"
        )
        day_el = self.driver.find_element(By.CSS_SELECTOR, day_css)
        self.driver.execute_script("arguments[0].click();", day_el)
        return self

    def set_subjects(self, *subjects):
        field = self.driver.find_element(*self.SUBJECTS)
        for subject in subjects:
            field.send_keys(subject)
            field.send_keys(Keys.ENTER)
        return self

    def set_hobbies(self, *hobbies):
        for hobby in hobbies:
            label = self.driver.find_element(
                By.XPATH, f"//div[@id='hobbiesWrapper']//label[.//input[@value='{hobby}']]"
            )
            self.driver.execute_script("arguments[0].click();", label)
        return self

    def upload_picture(self, path):
        self.driver.find_element(*self.UPLOAD).send_keys(path)
        return self

    def set_address(self, value):
        self.driver.find_element(*self.ADDRESS).send_keys(value)
        return self

    def set_state_city(self, state, city):
        self.driver.find_element(*self.STATE).click()
        self.wait.until(
            ec.element_to_be_clickable(
                (By.XPATH, f"//div[@class='state-city-option'][text()='{state}']")
            )
        ).click()
        self.driver.find_element(*self.CITY).click()
        self.wait.until(
            ec.element_to_be_clickable(
                (By.XPATH, f"//div[@class='state-city-option'][text()='{city}']")
            )
        ).click()
        return self

    def submit_form(self):
        self._close_overlays()
        btn = self.driver.find_element(*self.SUBMIT)
        self.driver.execute_script("arguments[0].click();", btn)
        return self

    def result_text(self):
        modal = self.wait.until(ec.visibility_of_element_located(self.RESULT))
        return modal.text

    @staticmethod
    def format_birth(year, month, day):
        months = [
            "Jan", "Feb", "Mar", "Apr", "May", "Jun",
            "Jul", "Aug", "Sep", "Oct", "Nov", "Dec",
        ]
        return f"{int(day)} {months[int(month)]} {year}"
