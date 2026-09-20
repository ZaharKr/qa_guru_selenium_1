from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from chrome_setup import TEXT_BOX_URL, create_driver, js_click


def test_textbox_explicit_wait():
    driver = create_driver()
    try:
        driver.get(TEXT_BOX_URL)
        w = WebDriverWait(driver, 10)

        w.until(EC.element_to_be_clickable((By.ID, "userName"))).send_keys("Анна Тест")
        driver.find_element(By.ID, "userEmail").send_keys("anna@test.ru")
        driver.find_element(By.ID, "currentAddress").send_keys("Москва")
        driver.find_element(By.ID, "permanentAddress").send_keys("СПб")

        js_click(driver, driver.find_element(By.ID, "submit"))

        output = w.until(EC.visibility_of_element_located((By.ID, "output")))
        assert "Анна Тест" in output.text
        assert "anna@test.ru" in output.text
        assert "Москва" in output.text
        assert "СПб" in output.text
        print("OK: textbox explicit wait")
    finally:
        driver.quit()


def test_textbox_fluent_wait():
    driver = create_driver()
    try:
        driver.get(TEXT_BOX_URL)
        driver.find_element(By.ID, "userName").send_keys("Fluent User")
        driver.find_element(By.ID, "userEmail").send_keys("fluent@test.ru")
        js_click(driver, driver.find_element(By.ID, "submit"))

        fluent = WebDriverWait(
            driver,
            timeout=10,
            poll_frequency=0.3,
            ignored_exceptions=[NoSuchElementException, StaleElementReferenceException],
        )
        output = fluent.until(EC.visibility_of_element_located((By.ID, "output")))
        assert "Fluent User" in output.text
        print("OK: textbox fluent wait")
    finally:
        driver.quit()


def test_textbox_clear_and_refill():
    driver = create_driver()
    try:
        driver.get(TEXT_BOX_URL)
        name = driver.find_element(By.ID, "userName")
        name.send_keys("old name")
        name.clear()
        name.send_keys("new name")
        driver.find_element(By.ID, "userEmail").send_keys("new@test.ru")
        js_click(driver, driver.find_element(By.ID, "submit"))

        output = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.ID, "output")))
        assert "new name" in output.text
        assert "old name" not in output.text
        print("OK: clear and refill")
    finally:
        driver.quit()


if __name__ == "__main__":
    test_textbox_explicit_wait()
    test_textbox_fluent_wait()
    test_textbox_clear_and_refill()
