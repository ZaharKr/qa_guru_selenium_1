from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from chrome_setup import TEXT_BOX_URL, create_driver, js_click

base_url = TEXT_BOX_URL


def test_fluent_wait():
    driver = create_driver()
    try:
        driver.get(base_url)
        driver.find_element(By.ID, "userName").send_keys("Иван Иванов")
        driver.find_element(By.ID, "userEmail").send_keys("ivan@example.com")
        driver.find_element(By.ID, "currentAddress").send_keys("ул. Ленина, дом 1")
        driver.find_element(By.ID, "permanentAddress").send_keys("ул. Пушкина, дом 10")
        js_click(driver, driver.find_element(By.ID, "submit"))

        fluent_wait = WebDriverWait(
            driver,
            timeout=10,
            poll_frequency=0.5,
            ignored_exceptions=[NoSuchElementException, StaleElementReferenceException],
        )
        output_block = fluent_wait.until(EC.visibility_of_element_located((By.ID, "output")))
        assert output_block.is_displayed()
        print("Тест №1 успешно пройден!")
    finally:
        driver.quit()


def test_fluent_empty_wait():
    driver = create_driver()
    try:
        driver.get(base_url)
        js_click(driver, driver.find_element(By.ID, "submit"))

        fluent_wait = WebDriverWait(
            driver,
            timeout=5,
            poll_frequency=0.5,
            ignored_exceptions=[NoSuchElementException, StaleElementReferenceException],
        )
        output_block = fluent_wait.until(EC.visibility_of_element_located((By.ID, "output")))
        assert output_block.is_displayed()
        print("Тест №2 успешно пройден!")
    finally:
        driver.quit()


if __name__ == "__main__":
    test_fluent_wait()
    test_fluent_empty_wait()
