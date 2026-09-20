import os

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from seleniumpagefactory.Pagefactory import PageFactory


@pytest.fixture
def driver():
    opts = Options()
    opts.add_argument("--headless=new")
    opts.add_argument("--window-size=1400,1000")
    browser = webdriver.Chrome(options=opts)
    browser.implicitly_wait(3)
    yield browser
    browser.quit()


class BasePage(PageFactory):
    def __init__(self, driver):
        self.driver = driver
        self.timeout = 10

    def open_url(self, url: str):
        self.driver.get(url)
        return self


class AutomationPracticeFormPage(BasePage):
    locators = {
        "first_name": ("ID", "firstName"),
        "last_name": ("ID", "lastName"),
        "user_email": ("ID", "userEmail"),
        "banner_button": ("XPATH", "//div[@id='fixedban']//button[@aria-label='Close']"),
        "gender_male": ("XPATH", "//label[@for='gender-radio-1']"),
        "gender_female": ("XPATH", "//label[@for='gender-radio-2']"),
        "gender_other": ("XPATH", "//label[@for='gender-radio-3']"),
        "user_number": ("ID", "userNumber"),
        "date_of_birth_input": ("ID", "dateOfBirthInput"),
        "calendar_month_select": ("CLASS_NAME", "react-datepicker__month-select"),
        "calendar_year_select": ("CLASS_NAME", "react-datepicker__year-select"),
        "subjects_input": ("ID", "subjectsInput"),
        "hobby_sports": ("XPATH", "//label[@for='hobbies-checkbox-1']"),
        "hobby_reading": ("XPATH", "//label[@for='hobbies-checkbox-2']"),
        "hobby_music": ("XPATH", "//label[@for='hobbies-checkbox-3']"),
        "upload_picture_btn": ("ID", "uploadPicture"),
        "current_address": ("ID", "currentAddress"),
        "state_dropdown": ("ID", "state"),
        "city_dropdown": ("ID", "city"),
        "submit_button": ("ID", "submit"),
        "result_modal": ("ID", "resultModal"),
    }

    def _close_commercial_banner(self):
        self.driver.execute_script(
            "const b=document.getElementById('fixedban'); if(b) b.remove();"
            "const f=document.getElementsByTagName('footer')[0]; if(f) f.style.display='none';"
        )

    def fill_personal_info(self, first_name, last_name, email, gender, mobile):
        self._close_commercial_banner()
        self.first_name.clear_text()
        self.first_name.set_text(first_name)
        self.last_name.set_text(last_name)
        self.user_email.set_text(email)

        gender_map = {
            "male": self.gender_male,
            "female": self.gender_female,
            "other": self.gender_other,
        }
        gender_el = gender_map[gender.lower()]
        gender_el.hover()
        gender_el.scroll_into_view()
        self.driver.execute_script("arguments[0].click();", gender_el)

        # is_Enabled() в PF ломается на Selenium 4 (Java API) — берём нативный метод
        assert self.user_number.is_enabled()
        self.user_number.set_text(mobile)
        return self

    def select_date_of_birth(self, year, month, day):
        # month — индекс в react-datepicker (0=January)
        self.date_of_birth_input.click_button()
        self.calendar_year_select.select_element_by_value(year)
        months_count = self.calendar_month_select.get_list_item_count()
        assert months_count == 12
        self.calendar_month_select.select_element_by_value(month)
        day_css = (
            f".react-datepicker__day--{int(day):03d}"
            f":not(.react-datepicker__day--outside-month)"
        )
        self.driver.find_element(By.CSS_SELECTOR, day_css).click()
        return self

    def enter_subjects(self, subjects):
        for subject in subjects:
            self.subjects_input.set_text(subject)
            self.subjects_input.send_keys(Keys.ENTER)
        return self

    def select_hobbies(self, hobbies):
        hobbies_map = {
            "sports": self.hobby_sports,
            "reading": self.hobby_reading,
            "music": self.hobby_music,
        }
        for hobby in hobbies:
            el = hobbies_map[hobby.lower()]
            el.scroll_into_view()
            self.driver.execute_script("arguments[0].click();", el)
        return self

    def upload_file(self, file_path):
        self.upload_picture_btn.send_keys(file_path)
        assert self.upload_picture_btn.get_attribute("type") == "file"
        return self

    def fill_address_and_location(self, address, state, city):
        self.current_address.set_text(address)
        self.state_dropdown.scroll_into_view()
        self.state_dropdown.click_button()
        self.driver.find_element(
            By.XPATH, f"//div[@class='state-city-option'][text()='{state}']"
        ).click()
        self.city_dropdown.click_button()
        self.driver.find_element(
            By.XPATH, f"//div[@class='state-city-option'][text()='{city}']"
        ).click()
        return self

    def submit_form(self):
        self.submit_button.scroll_into_view()
        self.driver.execute_script("arguments[0].click();", self.submit_button)
        return self

    def fill_form(
        self,
        first_name,
        last_name,
        email,
        gender,
        mobile,
        year,
        month,
        day,
        subjects,
        hobbies,
        file_path,
        address,
        state,
        city,
    ):
        return (
            self.fill_personal_info(first_name, last_name, email, gender, mobile)
            .select_date_of_birth(year, month, day)
            .enter_subjects(subjects)
            .select_hobbies(hobbies)
            .upload_file(file_path)
            .fill_address_and_location(address, state, city)
            .submit_form()
        )

    def get_result_text(self):
        self.result_modal.visibility_of_element_located()
        return self.result_modal.get_text()


FORM_CASES = [
    {
        "first_name": "Ivan",
        "last_name": "Ivanov",
        "email": "ivanov@university.edu",
        "gender": "Male",
        "mobile": "1234567890",
        "year": "2000",
        "month": "0",
        "day": "15",
        "subjects": ["Maths", "Computer Science"],
        "hobbies": ["Sports", "Music"],
        "address": "123 University Avenue, Tomsk, Russia",
        "state": "NCR",
        "city": "Delhi",
        "birth_label": "15 Jan 2000",
    },
    {
        "first_name": "Anna",
        "last_name": "Smirnova",
        "email": "anna@mail.ru",
        "gender": "Female",
        "mobile": "9001112233",
        "year": "1995",
        "month": "11",
        "day": "05",
        "subjects": ["English"],
        "hobbies": ["Reading"],
        "address": "Москва, Тверская 1",
        "state": "NCR",
        "city": "Noida",
        "birth_label": "5 Dec 1995",
    },
]


@pytest.mark.parametrize("case", FORM_CASES, ids=["ivan", "anna"])
def test_student_registration_form_max_capabilities(driver, case):
    test_filename = "demo_upload.txt"
    with open(test_filename, "w") as f:
        f.write("QA Guru PageFactory Demo File Content")
    abs_file_path = os.path.abspath(test_filename)

    try:
        page = AutomationPracticeFormPage(driver)
        page.open_url(
            "https://qa-guru.github.io/one-page-form/automation-practice-form.html"
        )
        page.fill_form(
            first_name=case["first_name"],
            last_name=case["last_name"],
            email=case["email"],
            gender=case["gender"],
            mobile=case["mobile"],
            year=case["year"],
            month=case["month"],
            day=case["day"],
            subjects=case["subjects"],
            hobbies=case["hobbies"],
            file_path=abs_file_path,
            address=case["address"],
            state=case["state"],
            city=case["city"],
        )

        text = page.get_result_text()
        assert f"{case['first_name']} {case['last_name']}" in text
        assert case["email"] in text
        assert case["gender"] in text
        assert case["mobile"] in text
        assert case["birth_label"] in text
        for subject in case["subjects"]:
            assert subject in text
        for hobby in case["hobbies"]:
            assert hobby in text
        assert test_filename in text
        assert case["address"] in text
        assert case["state"] in text and case["city"] in text
    finally:
        if os.path.exists(abs_file_path):
            os.remove(abs_file_path)
