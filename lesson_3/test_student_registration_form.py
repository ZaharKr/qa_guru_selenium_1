import os

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

from chrome_setup import REG_URL, create_driver, hide_overlays, js_click, wait


def test_student_registration_required_fields():
    driver = create_driver()
    w = wait(driver, 10)
    try:
        driver.get(REG_URL)
        hide_overlays(driver)

        w.until(EC.element_to_be_clickable((By.ID, "firstName"))).send_keys("Мария")
        driver.find_element(By.ID, "lastName").send_keys("Иванова")
        w.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "label[for='gender-radio-2']"))).click()
        driver.find_element(By.ID, "userNumber").send_keys("9001112233")

        js_click(driver, driver.find_element(By.ID, "submit"))

        modal = w.until(EC.visibility_of_element_located((By.ID, "example-modal-sizes-title-lg")))
        assert modal.text == "Thanks for submitting the form"
        table = driver.find_element(By.ID, "resultBody").text
        assert "Мария Иванова" in table
        assert "Female" in table
        assert "9001112233" in table
        print("OK: registration required fields")
    finally:
        driver.quit()


def test_student_registration_full():
    driver = create_driver()
    w = wait(driver, 10)
    temp = os.path.abspath("pic_test.txt")
    try:
        driver.get(REG_URL)
        hide_overlays(driver)

        w.until(EC.element_to_be_clickable((By.ID, "firstName"))).send_keys("Иван")
        driver.find_element(By.ID, "lastName").send_keys("Петров")
        driver.find_element(By.ID, "userEmail").send_keys("ivan.petrov@example.com")
        w.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "label[for='gender-radio-1']"))).click()
        driver.find_element(By.ID, "userNumber").send_keys("9991234567")

        driver.find_element(By.ID, "dateOfBirthInput").click()
        w.until(EC.visibility_of_element_located((By.CLASS_NAME, "react-datepicker")))
        driver.find_element(By.CLASS_NAME, "react-datepicker__month-select").send_keys("December")
        driver.find_element(By.CLASS_NAME, "react-datepicker__year-select").send_keys("1995")
        driver.find_element(
            By.CSS_SELECTOR,
            ".react-datepicker__day--025:not(.react-datepicker__day--outside-month)",
        ).click()

        subjects = driver.find_element(By.ID, "subjectsInput")
        subjects.send_keys("Maths")
        subjects.send_keys(Keys.ENTER)

        w.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "label[for='hobbies-checkbox-2']"))).click()

        with open(temp, "w") as f:
            f.write("x")
        driver.find_element(By.ID, "uploadPicture").send_keys(temp)

        driver.find_element(By.ID, "currentAddress").send_keys("Москва, Тверская 1")
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        hide_overlays(driver)

        w.until(EC.element_to_be_clickable((By.ID, "state"))).click()
        w.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='stateCity-wrapper']/div[text()='NCR']"))).click()
        w.until(EC.element_to_be_clickable((By.ID, "city"))).click()
        w.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='stateCity-wrapper']/div[text()='Delhi']"))).click()

        js_click(driver, driver.find_element(By.ID, "submit"))

        w.until(EC.visibility_of_element_located((By.ID, "example-modal-sizes-title-lg")))
        table = driver.find_element(By.CLASS_NAME, "table-responsive").text
        assert "Иван Петров" in table
        assert "Reading" in table
        assert "Maths" in table
        assert "NCR Delhi" in table or ("NCR" in table and "Delhi" in table)
        print("OK: registration full form")
    finally:
        if os.path.exists(temp):
            os.remove(temp)
        driver.quit()


def test_student_registration_negative_empty():
    driver = create_driver()
    w = wait(driver, 10)
    try:
        driver.get(REG_URL)
        hide_overlays(driver)
        js_click(driver, driver.find_element(By.ID, "submit"))
        err = w.until(EC.visibility_of_element_located((By.ID, "formError")))
        assert err.text
        print("OK: registration empty negative")
    finally:
        driver.quit()


if __name__ == "__main__":
    test_student_registration_required_fields()
    test_student_registration_full()
    test_student_registration_negative_empty()
