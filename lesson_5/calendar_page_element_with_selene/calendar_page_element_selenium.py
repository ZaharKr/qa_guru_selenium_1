from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait


class Calendar:
    def __init__(self, driver, input_locator):
        self.driver = driver
        self.input_locator = input_locator
        self.wait = WebDriverWait(driver, 10)

    def close_banner(self):
        try:
            btn = self.wait.until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//*[@id='fixedban']//button[@aria-label='Close']")
                )
            )
            btn.click()
            self.wait.until(EC.invisibility_of_element(btn))
        except Exception:
            self.driver.execute_script(
                "const b=document.getElementById('fixedban'); if(b) b.remove();"
            )

    def select_date(self, day: str, month: str, year: str):
        self.close_banner()
        self.driver.find_element(*self.input_locator).click()
        Select(self.driver.find_element(By.CSS_SELECTOR, ".react-datepicker__month-select")).select_by_visible_text(month)
        Select(self.driver.find_element(By.CSS_SELECTOR, ".react-datepicker__year-select")).select_by_visible_text(year)
        day_padded = f"{int(day):03d}"
        self.driver.find_element(
            By.CSS_SELECTOR,
            f".react-datepicker__day--{day_padded}:not(.react-datepicker__day--outside-month)",
        ).click()


class AutomationPracticeFormPage:
    def __init__(self, driver):
        self.driver = driver
        self.driver.get("https://qa-guru.github.io/one-page-form/automation-practice-form.html")
        self.birthday_calendar = Calendar(driver, (By.ID, "dateOfBirthInput"))


if __name__ == "__main__":
    opts = Options()
    opts.add_argument("--headless=new")
    opts.add_argument("--window-size=1400,1000")
    driver = webdriver.Chrome(options=opts)
    try:
        page = AutomationPracticeFormPage(driver)
        page.birthday_calendar.select_date(day="15", month="July", year="2000")
        value = driver.find_element(By.ID, "dateOfBirthInput").get_attribute("value")
        assert value == "15 Jul 2000", value
        print("OK: calendar selenium")
    finally:
        driver.quit()
