import time

from selenium.webdriver.common.by import By

from chrome_setup import PAUSE, URL, click_submit, create_driver


def test01():
    print("Рефакторинг - итерация 1!")

    driver = create_driver()

    try:
        driver.get(URL)
        driver.maximize_window()
        time.sleep(PAUSE)

        full_name = "Анна Смирнова"
        email = "anna.smirnova@example.com"

        driver.find_element(By.ID, "userName").send_keys(full_name)
        driver.find_element(By.ID, "userEmail").send_keys(email)
        click_submit(driver)
        time.sleep(PAUSE)

        result_box = driver.find_element(By.ID, "output")
        assert full_name in result_box.text
        assert email in result_box.text
        print("Тест успешно пройден!")

    finally:
        driver.quit()


def test02():
    print("Рефакторинг - итерация 1!")

    driver = create_driver()

    try:
        driver.get(URL)
        driver.maximize_window()
        time.sleep(PAUSE)

        bad_email = "annaexample.com"

        driver.find_element(By.ID, "userName").send_keys("Анна Смирнова")
        email_field = driver.find_element(By.ID, "userEmail")
        email_field.send_keys(bad_email)
        click_submit(driver)
        time.sleep(PAUSE)

        # без @ форма не должна отправиться
        assert not email_field.get_property("validity")["valid"]
        output = driver.find_element(By.ID, "output")
        assert "has-content" not in (output.get_attribute("class") or "")
        print("Тест успешно пройден!")

    finally:
        driver.quit()


test01()
test02()
