from typing import Tuple

from selenium import webdriver
from selenium.common.exceptions import InvalidSelectorException, NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

from calendar_element import CalendarElement


class AutomationPracticeFormPO:
    def __init__(self, url):
        self.url = url

    PRACTICE_FORM_TITLE = (By.XPATH, "//main//h1")
    FIRST_NAME_FIELD = (By.ID, "firstName")
    LAST_NAME_FIELD = (By.ID, "lastName")
    EMAIL_FIELD = (By.ID, "userEmail")
    USER_NUMBER_FIELD = (By.ID, "userNumber")
    CALENDAR_INPUT = (By.ID, "dateOfBirthInput")
    SUBJECT_FIELD = (By.ID, "subjectsInput")
    UPLOAD_PICTURE_BUTTON = (By.ID, "uploadPicture")
    CURRENT_ADDRESS_FIELD = (By.ID, "currentAddress")
    STATE_INPUT = (By.ID, "state")
    CITY_INPUT = (By.ID, "city")
    SUBMIT_BUTTON = (By.ID, "submit")
    BANNER_BUTTON = (By.XPATH, "//div[@id='fixedban']//button[@aria-label='Close']")
    RESULT_FORM = (By.ID, "resultModal")

    def setup(self):
        opts = Options()
        opts.add_argument("--headless=new")
        opts.add_argument("--window-size=1400,1000")
        self.driver = webdriver.Chrome(options=opts)
        self.driver.implicitly_wait(5)
        self.wait = WebDriverWait(self.driver, 10)
        self.driver.get(self.url)
        self.calendar = CalendarElement(self.driver, self.CALENDAR_INPUT)

    def _close_commercial_banner(self):
        try:
            banner_button = self.wait.until(ec.element_to_be_clickable(self.BANNER_BUTTON))
            banner_button.click()
            self.wait.until(ec.invisibility_of_element(banner_button))
        except Exception:
            self.driver.execute_script(
                "const b=document.getElementById('fixedban'); if(b) b.remove();"
            )

    def _fill_first_name(self, first_name):
        self.driver.find_element(*self.FIRST_NAME_FIELD).send_keys(first_name)

    def _fill_last_name(self, last_name):
        self.driver.find_element(*self.LAST_NAME_FIELD).send_keys(last_name)

    def _fill_email(self, email):
        self.driver.find_element(*self.EMAIL_FIELD).send_keys(email)

    def _fill_user_number(self, user_number):
        self.driver.find_element(*self.USER_NUMBER_FIELD).send_keys(user_number)

    def _select_gender(self, gender):
        label = self.driver.find_element(
            By.XPATH, f"//div[@id='genterWrapper']//label[.//input[@value='{gender}']]"
        )
        self.driver.execute_script("arguments[0].click();", label)

    def _select_birth_day(self, date: Tuple[str, str, str]):
        self.calendar.select_date(date[0], date[1], date[2])

    def _upload_file(self, file_path):
        self.driver.find_element(*self.UPLOAD_PICTURE_BUTTON).send_keys(file_path)

    def _fill_subject(self, subjects):
        subjects_input = self.driver.find_element(*self.SUBJECT_FIELD)
        self.driver.execute_script("arguments[0].scrollIntoView();", subjects_input)
        for subject in subjects:
            subjects_input.send_keys(subject)
            subjects_input.send_keys(Keys.ENTER)

    def _select_hobbies(self, hobbies):
        for hobby in hobbies:
            label = self.driver.find_element(
                By.XPATH, f"//div[@id='hobbiesWrapper']//label[.//input[@value='{hobby}']]"
            )
            self.driver.execute_script("arguments[0].click();", label)

    def _fill_current_address(self, current_address):
        self.driver.find_element(*self.CURRENT_ADDRESS_FIELD).send_keys(current_address)

    def _select_state(self, state):
        self.driver.find_element(*self.STATE_INPUT).click()
        opt = self.wait.until(
            ec.element_to_be_clickable(
                (By.XPATH, f"//div[@class='state-city-option'][text()='{state}']")
            )
        )
        opt.click()

    def _select_city(self, city):
        self.driver.find_element(*self.CITY_INPUT).click()
        opt = self.wait.until(
            ec.element_to_be_clickable(
                (By.XPATH, f"//div[@class='state-city-option'][text()='{city}']")
            )
        )
        opt.click()

    def _click_submit_button(self):
        submit_button = self.driver.find_element(*self.SUBMIT_BUTTON)
        self.driver.execute_script("arguments[0].click();", submit_button)

    def fill_in_form(
        self,
        file_name=None,
        first_name=None,
        last_name=None,
        email=None,
        gender=None,
        user_number=None,
        birth_day=None,
        subjects=None,
        hobbies=None,
        current_address=None,
        state=None,
        city=None,
    ):
        title = self.driver.find_element(*self.PRACTICE_FORM_TITLE)
        assert title.text == "Practice Form"

        self._close_commercial_banner()
        self._fill_first_name(first_name)
        self._fill_last_name(last_name)
        self._fill_email(email)
        self._select_gender(gender)
        self._fill_user_number(user_number)
        self._select_birth_day(birth_day)
        self._fill_subject(subjects)
        self._select_hobbies(hobbies)
        self._upload_file(file_name)
        self._fill_current_address(current_address)
        self.driver.execute_script(
            "document.getElementsByTagName('footer')[0].style.display='none';"
        )
        self._select_state(state)
        self._select_city(city)
        self._click_submit_button()

    def assert_student_name(self, first_name, last_name):
        text = self._result_text()
        assert f"{first_name} {last_name}" in text

    def assert_contacts(self, email, user_number):
        text = self._result_text()
        assert email in text
        assert user_number in text

    def assert_form(
        self,
        file_name=None,
        first_name=None,
        last_name=None,
        email=None,
        gender=None,
        user_number=None,
        birth_day=None,
        subjects=None,
        hobbies=None,
        current_address=None,
        state=None,
        city=None,
    ):
        text = self._result_text()
        assert f"{first_name} {last_name}" in text
        assert email in text
        assert gender in text
        assert user_number in text
        assert CalendarElement.format_for_result(*birth_day) in text
        for subject in subjects:
            assert subject in text
        for hobby in hobbies:
            assert hobby in text
        assert "test_file.jpg" in text
        assert current_address in text
        assert state in text and city in text

    def _result_text(self):
        result_form = self.wait.until(ec.visibility_of_element_located(self.RESULT_FORM))
        assert result_form.is_displayed()
        return result_form.text

    def tear_down(self):
        self.driver.quit()
