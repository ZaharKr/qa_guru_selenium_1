from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class CalendarElement:
    YEAR_SELECT = (By.CSS_SELECTOR, ".react-datepicker__year-select")
    MONTH_SELECT = (By.CSS_SELECTOR, ".react-datepicker__month-select")

    def __init__(self, driver, input_locator):
        self.driver = driver
        self.input_locator = input_locator

    def select_date(self, year: str, month: str, day: str):
        self.driver.find_element(*self.input_locator).click()
        Select(self.driver.find_element(*self.YEAR_SELECT)).select_by_value(year)
        Select(self.driver.find_element(*self.MONTH_SELECT)).select_by_value(month)
        day_css = f".react-datepicker__day--{int(day):03d}:not(.react-datepicker__day--outside-month)"
        self.driver.find_element(By.CSS_SELECTOR, day_css).click()

    @staticmethod
    def format_for_result(year: str, month: str, day: str) -> str:
        months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        return f"{int(day)} {months[int(month)]} {year}"
