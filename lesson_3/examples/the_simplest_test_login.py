# примеры с занятия — чуть подправлены чтобы стабильно бежали (headless + короткие паузы)

import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from chrome_setup import LOGIN_URL, create_driver, js_click

LOGIN_INPUT = (By.ID, "login-input")
PASSWORD_INPUT = (By.ID, "password-input")
SUBMIT_BUTTON = (By.ID, "submit-button")
STATUS_MESSAGE = (By.ID, "error-message")

driver = create_driver()

try:
    driver.get(LOGIN_URL)
    driver.implicitly_wait(5)
    wait = WebDriverWait(driver, 20)

    driver.find_element(*LOGIN_INPUT).send_keys("qaguru@gmail.com")
    driver.find_element(*PASSWORD_INPUT).send_keys("qagurupassword")

    submit_button = wait.until(EC.element_to_be_clickable(SUBMIT_BUTTON))
    js_click(driver, submit_button)

    error_message = driver.find_element(*STATUS_MESSAGE).text
    time.sleep(1)

    assert "Wrong login or password" in error_message
    print("Тест пройден успешно!")

finally:
    driver.quit()
