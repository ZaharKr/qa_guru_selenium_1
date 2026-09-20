from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from chrome_setup import LOGIN_URL, create_driver, js_click


def open_clean(driver):
    driver.get(LOGIN_URL)
    driver.execute_script("localStorage.clear();")
    driver.get(LOGIN_URL)


def test_login_success_with_wait():
    driver = create_driver()
    try:
        open_clean(driver)
        w = WebDriverWait(driver, 10)

        w.until(EC.element_to_be_clickable((By.ID, "login-input"))).send_keys("user1")
        driver.find_element(By.ID, "password-input").send_keys("password1")
        js_click(driver, driver.find_element(By.ID, "submit-button"))

        panel = w.until(EC.visibility_of_element_located((By.ID, "success-panel")))
        assert "is-visible" in (panel.get_attribute("class") or "")
        assert "user1" in driver.find_element(By.ID, "welcome-message").text
        print("OK: login success wait")
    finally:
        driver.quit()


def test_login_error_with_wait():
    driver = create_driver()
    try:
        open_clean(driver)
        w = WebDriverWait(driver, 10)

        w.until(EC.element_to_be_clickable((By.ID, "login-input"))).send_keys("user1")
        driver.find_element(By.ID, "password-input").send_keys("badpass")
        js_click(driver, driver.find_element(By.ID, "submit-button"))

        err = w.until(EC.visibility_of_element_located((By.ID, "error-message")))
        assert "Wrong login or password" in err.text
        print("OK: login error wait")
    finally:
        driver.quit()


if __name__ == "__main__":
    test_login_success_with_wait()
    test_login_error_with_wait()
