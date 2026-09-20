import time

from selenium.webdriver.common.by import By

from chrome_setup import LOGIN_URL, PAUSE, click_login_submit, create_driver

LOGIN_INPUT = (By.ID, "login-input")
PASSWORD_INPUT = (By.ID, "password-input")
STATUS_MESSAGE = (By.ID, "error-message")

driver = create_driver()

try:
    driver.get(LOGIN_URL)
    driver.maximize_window()
    driver.implicitly_wait(5)

    driver.find_element(*LOGIN_INPUT).send_keys("qaguru@gmail.com")
    driver.find_element(*PASSWORD_INPUT).send_keys("qagurupassword")
    click_login_submit(driver)

    error_message = driver.find_element(*STATUS_MESSAGE).text
    time.sleep(PAUSE)

    assert "Wrong login or password" in error_message
    print("Тест пройден успешно!")

finally:
    driver.quit()
