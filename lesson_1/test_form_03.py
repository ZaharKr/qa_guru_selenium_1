import time

from selenium.webdriver.common.by import By

from chrome_setup import PAUSE, URL, click_submit, create_driver

FULL_NAME = "Пётр Петров"
EMAIL = "petr.petrov@mail.ru"

driver = create_driver()

try:
    driver.get(URL)
    driver.maximize_window()
    time.sleep(PAUSE)

    driver.find_element(By.ID, "userName").send_keys(FULL_NAME)
    driver.find_element(By.ID, "userEmail").send_keys(EMAIL)
    click_submit(driver)
    time.sleep(PAUSE)

    result_box = driver.find_element(By.ID, "output")
    assert FULL_NAME in result_box.text
    assert EMAIL in result_box.text
    print("Тест успешно пройден!")

finally:
    driver.quit()
