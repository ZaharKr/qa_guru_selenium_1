import pytest
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
SUCCESS_PANEL = (By.ID, "success-panel")
WELCOME = (By.ID, "welcome-message")


@pytest.fixture
def driver():
    driver = create_driver()
    driver.implicitly_wait(5)
    yield driver
    driver.quit()


@pytest.mark.parametrize(
    "login, password, kind, expected",
    [
        ("user1", "password1", "positive", "Welcome, user1!"),
        ("user1", "wrongpass", "negative", "Wrong login or password"),
        ("unknown", "password1", "negative", "Wrong login or password"),
        ("", "", "negative", "Login and password are required"),
        ("", "password1", "negative", "Login is required"),
        ("user1", "", "negative", "Password is required"),
        ("ab", "password1", "negative", "at least 3 characters"),
        ("user1", "12345", "negative", "at least 6 characters"),
        ("' OR '1'='1", "' OR '1'='1", "negative", "Wrong login or password"),
    ],
)
def test_login_form(driver, login, password, kind, expected):
    driver.get(LOGIN_URL)
    driver.execute_script("localStorage.clear();")
    driver.get(LOGIN_URL)

    driver.find_element(*LOGIN_INPUT).clear()
    driver.find_element(*PASSWORD_INPUT).clear()
    if login:
        driver.find_element(*LOGIN_INPUT).send_keys(login)
    if password:
        driver.find_element(*PASSWORD_INPUT).send_keys(password)

    js_click(driver, driver.find_element(*SUBMIT_BUTTON))

    if kind == "positive":
        panel = WebDriverWait(driver, 5).until(EC.visibility_of_element_located(SUCCESS_PANEL))
        assert "is-visible" in (panel.get_attribute("class") or "")
        assert expected in driver.find_element(*WELCOME).text
    else:
        text = WebDriverWait(driver, 5).until(EC.visibility_of_element_located(STATUS_MESSAGE)).text
        assert expected in text
