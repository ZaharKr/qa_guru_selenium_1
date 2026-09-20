import os
import unittest

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from chrome_setup import REG_URL, create_driver, hide_overlays, js_click, wait


class TestAutomationForm(unittest.TestCase):

    def setUp(self):
        self.driver = create_driver()
        self.wait = wait(self.driver, 10)
        self.url = REG_URL

    def test_fill_entire_form(self):
        driver = self.driver
        w = self.wait
        driver.get(self.url)

        form_title = w.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "main section h1")))
        self.assertIn("Practice Form", form_title.text)

        hide_overlays(driver)

        w.until(EC.element_to_be_clickable((By.ID, "firstName"))).send_keys("Иван")
        driver.find_element(By.ID, "lastName").send_keys("Петров")
        driver.find_element(By.ID, "userEmail").send_keys("ivan.petrov@example.com")

        w.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "label[for='gender-radio-1']"))).click()
        driver.find_element(By.ID, "userNumber").send_keys("9991234567")

        driver.find_element(By.ID, "dateOfBirthInput").click()
        w.until(EC.visibility_of_element_located((By.CLASS_NAME, "react-datepicker__month-container")))
        month_select = w.until(EC.element_to_be_clickable((By.CLASS_NAME, "react-datepicker__month-select")))
        month_select.click()
        month_select.find_element(By.CSS_SELECTOR, "option[value='11']").click()
        year_select = driver.find_element(By.CLASS_NAME, "react-datepicker__year-select")
        year_select.click()
        year_select.find_element(By.CSS_SELECTOR, "option[value='1995']").click()
        driver.find_element(
            By.CSS_SELECTOR,
            ".react-datepicker__day--025:not(.react-datepicker__day--outside-month)",
        ).click()

        subjects = w.until(EC.element_to_be_clickable((By.ID, "subjectsInput")))
        subjects.send_keys("Computer Science")
        subjects.send_keys(Keys.ENTER)

        w.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "label[for='hobbies-checkbox-1']"))).click()
        driver.find_element(By.CSS_SELECTOR, "label[for='hobbies-checkbox-3']").click()

        temp_file_path = os.path.abspath("test_image.jpg")
        with open(temp_file_path, "w") as f:
            f.write("fake image data")
        driver.find_element(By.ID, "uploadPicture").send_keys(temp_file_path)

        driver.find_element(By.ID, "currentAddress").send_keys("123456, г. Москва, ул. Ленина, д. 1")

        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        hide_overlays(driver)

        w.until(EC.element_to_be_clickable((By.ID, "state"))).click()
        w.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='stateCity-wrapper']/div[1]"))).click()
        w.until(EC.element_to_be_clickable((By.ID, "city"))).click()
        w.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='stateCity-wrapper']/div[1]"))).click()

        js_click(driver, driver.find_element(By.ID, "submit"))

        modal_title = w.until(EC.visibility_of_element_located((By.ID, "example-modal-sizes-title-lg")))
        self.assertEqual(modal_title.text, "Thanks for submitting the form")

        result_table = driver.find_element(By.CLASS_NAME, "table-responsive")
        self.assertIn("Иван Петров", result_table.text)
        self.assertIn("ivan.petrov@example.com", result_table.text)
        self.assertIn("Male", result_table.text)
        self.assertIn("9991234567", result_table.text)
        self.assertIn("25 Dec 1995", result_table.text)
        self.assertIn("Computer Science", result_table.text)
        self.assertIn("Sports", result_table.text)
        self.assertIn("Music", result_table.text)
        self.assertIn("test_image.jpg", result_table.text)
        self.assertIn("123456, г. Москва, ул. Ленина, д. 1", result_table.text)
        self.assertIn("NCR", result_table.text)
        self.assertIn("Delhi", result_table.text)

    def tearDown(self):
        if os.path.exists("test_image.jpg"):
            os.remove("test_image.jpg")
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
