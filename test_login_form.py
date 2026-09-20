import time

from selenium.webdriver.common.by import By

from chrome_setup import LOGIN_URL, PAUSE, click_element, click_login_submit, create_driver

LOGIN_INPUT = (By.ID, "login-input")
PASSWORD_INPUT = (By.ID, "password-input")
ERROR_MESSAGE = (By.ID, "error-message")
SUCCESS_PANEL = (By.ID, "success-panel")
WELCOME = (By.ID, "welcome-message")
LOGOUT = (By.ID, "logout-button")

VALID_LOGIN = "user1"
VALID_PASSWORD = "password1"


def open_login(driver):
    driver.get(LOGIN_URL)
    driver.delete_all_cookies()
    driver.execute_script("localStorage.clear();")
    driver.get(LOGIN_URL)
    time.sleep(PAUSE)


def login(driver, login_value, password_value):
    driver.find_element(*LOGIN_INPUT).clear()
    driver.find_element(*PASSWORD_INPUT).clear()
    if login_value:
        driver.find_element(*LOGIN_INPUT).send_keys(login_value)
    if password_value:
        driver.find_element(*PASSWORD_INPUT).send_keys(password_value)
    click_login_submit(driver)
    time.sleep(PAUSE)


def test_success_login():
    driver = create_driver()
    try:
        open_login(driver)
        login(driver, VALID_LOGIN, VALID_PASSWORD)
        panel = driver.find_element(*SUCCESS_PANEL)
        assert "is-visible" in (panel.get_attribute("class") or "")
        assert VALID_LOGIN in driver.find_element(*WELCOME).text
        print("OK: success login")
    finally:
        driver.quit()


def test_wrong_password():
    driver = create_driver()
    try:
        open_login(driver)
        login(driver, VALID_LOGIN, "wrongpass")
        assert "Wrong login or password" in driver.find_element(*ERROR_MESSAGE).text
        print("OK: wrong password")
    finally:
        driver.quit()


def test_unknown_user():
    driver = create_driver()
    try:
        open_login(driver)
        login(driver, "unknown", "password1")
        assert "Wrong login or password" in driver.find_element(*ERROR_MESSAGE).text
        print("OK: unknown user")
    finally:
        driver.quit()


def test_empty_both():
    driver = create_driver()
    try:
        open_login(driver)
        login(driver, "", "")
        text = driver.find_element(*ERROR_MESSAGE).text
        assert "Login and password are required" in text
        print("OK: empty both")
    finally:
        driver.quit()


def test_empty_login():
    driver = create_driver()
    try:
        open_login(driver)
        login(driver, "", "password1")
        assert "Login is required" in driver.find_element(*ERROR_MESSAGE).text
        print("OK: empty login")
    finally:
        driver.quit()


def test_empty_password():
    driver = create_driver()
    try:
        open_login(driver)
        login(driver, "user1", "")
        assert "Password is required" in driver.find_element(*ERROR_MESSAGE).text
        print("OK: empty password")
    finally:
        driver.quit()


def test_short_login():
    driver = create_driver()
    try:
        open_login(driver)
        login(driver, "ab", "password1")
        assert "at least 3 characters" in driver.find_element(*ERROR_MESSAGE).text
        print("OK: short login")
    finally:
        driver.quit()


def test_short_password():
    driver = create_driver()
    try:
        open_login(driver)
        login(driver, "user1", "12345")
        assert "at least 6 characters" in driver.find_element(*ERROR_MESSAGE).text
        print("OK: short password")
    finally:
        driver.quit()


def test_sql_injection():
    driver = create_driver()
    try:
        open_login(driver)
        login(driver, "' OR '1'='1", "' OR '1'='1")
        assert "Wrong login or password" in driver.find_element(*ERROR_MESSAGE).text
        print("OK: sql injection")
    finally:
        driver.quit()


def test_json_injection():
    driver = create_driver()
    try:
        open_login(driver)
        login(driver, '{"admin":true}', "password1")
        err = driver.find_element(*ERROR_MESSAGE).text
        assert err
        print("OK: json injection")
    finally:
        driver.quit()


def test_logout():
    driver = create_driver()
    try:
        open_login(driver)
        login(driver, VALID_LOGIN, VALID_PASSWORD)
        click_element(driver, driver.find_element(*LOGOUT))
        time.sleep(PAUSE)
        assert driver.find_element(By.ID, "login-form").is_displayed()
        print("OK: logout")
    finally:
        driver.quit()


if __name__ == "__main__":
    test_success_login()
    test_wrong_password()
    test_unknown_user()
    test_empty_both()
    test_empty_login()
    test_empty_password()
    test_short_login()
    test_short_password()
    test_sql_injection()
    test_json_injection()
    test_logout()
    print("\nГотово login")
