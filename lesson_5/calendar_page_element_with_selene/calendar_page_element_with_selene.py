from selene import be, browser, by

# pip install selene


class Calendar:
    def __init__(self, base_element):
        self.input_field = base_element

    def close_banner(self):
        # убираем промо-баннер, который перекрывает календарь
        if browser.element("#fixedban").matching(be.visible):
            browser.element("#fixedban button[aria-label='Close']").click()
            browser.element("#fixedban").should(be.not_.visible)

    def select_date(self, day: str, month: str, year: str):
        self.close_banner()
        self.input_field.click()
        browser.element(".react-datepicker__month-select").click().element(by.text(month)).click()
        browser.element(".react-datepicker__year-select").click().element(by.text(year)).click()
        day_padded = f"{int(day):03d}"
        browser.element(
            f".react-datepicker__day--{day_padded}:not(.react-datepicker__day--outside-month)"
        ).click()


class AutomationPracticeFormPage:
    def __init__(self):
        browser.open("https://qa-guru.github.io/one-page-form/automation-practice-form.html")
        self.birthday_calendar = Calendar(browser.element("#dateOfBirthInput"))


class TestSuite:
    def test_select_birthday_date(self):
        browser.config.timeout = 10
        page = AutomationPracticeFormPage()
        page.birthday_calendar.select_date(day="15", month="July", year="2000")
        page.birthday_calendar.input_field.should(be.value("15 Jul 2000"))


if __name__ == "__main__":
    browser.config.driver_options = None
    from selenium.webdriver.chrome.options import Options

    opts = Options()
    opts.add_argument("--headless=new")
    opts.add_argument("--window-size=1400,1000")
    browser.config.driver_options = opts
    TestSuite().test_select_birthday_date()
    browser.quit()
    print("OK: calendar selene")
