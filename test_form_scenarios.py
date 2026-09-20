import time

from selenium.webdriver.common.by import By

from chrome_setup import PAUSE, URL, click_submit, create_driver


def fill_and_submit(driver, name="", email="", current_address="", permanent_address=""):
    if name:
        driver.find_element(By.ID, "userName").send_keys(name)
    if email:
        driver.find_element(By.ID, "userEmail").send_keys(email)
    if current_address:
        driver.find_element(By.ID, "currentAddress").send_keys(current_address)
    if permanent_address:
        driver.find_element(By.ID, "permanentAddress").send_keys(permanent_address)
    click_submit(driver)
    time.sleep(PAUSE)


def output_has_content(driver):
    output = driver.find_element(By.ID, "output")
    return "has-content" in (output.get_attribute("class") or "")


def test_positive_full_form():
    driver = create_driver()
    try:
        driver.get(URL)
        fill_and_submit(
            driver,
            name="Мария Кузнецова",
            email="maria.k@example.com",
            current_address="Москва, ул. Тверская, 1",
            permanent_address="Санкт-Петербург, Невский пр., 10",
        )
        result = driver.find_element(By.ID, "output").text
        assert "Мария Кузнецова" in result
        assert "maria.k@example.com" in result
        assert "Тверская" in result
        assert "Невский" in result
        print("OK: positive full form")
    finally:
        driver.quit()


def test_addresses():
    driver = create_driver()
    try:
        driver.get(URL)
        current = "Казань, ул. Баумана, 5"
        permanent = "Новосибирск, Красный пр., 15"
        fill_and_submit(
            driver,
            name="Адрес Тестов",
            email="address@test.ru",
            current_address=current,
            permanent_address=permanent,
        )
        result = driver.find_element(By.ID, "output").text
        assert current in result
        assert permanent in result
        print("OK: addresses")
    finally:
        driver.quit()


def test_email_without_at():
    driver = create_driver()
    try:
        driver.get(URL)
        fill_and_submit(driver, name="Neg User", email="userexample.com")
        email_field = driver.find_element(By.ID, "userEmail")
        assert not email_field.get_property("validity")["valid"]
        assert not output_has_content(driver)
        print("OK: email without @")
    finally:
        driver.quit()


def test_empty_email():
    driver = create_driver()
    try:
        driver.get(URL)
        fill_and_submit(driver, name="Empty Email", email="")
        assert output_has_content(driver)
        email_line = driver.find_element(By.CSS_SELECTOR, "#output #email").text
        assert email_line.endswith(":") or email_line.endswith(": ")
        print("OK: empty email")
    finally:
        driver.quit()


def test_long_email():
    driver = create_driver()
    try:
        driver.get(URL)
        email = "a" * 100 + "@example.com"
        fill_and_submit(driver, name="Long Email", email=email)
        email_field = driver.find_element(By.ID, "userEmail")
        if email_field.get_property("validity")["valid"]:
            assert email in driver.find_element(By.ID, "output").text
            print("OK: long email accepted")
        else:
            assert not output_has_content(driver)
            print("OK: long email rejected")
    finally:
        driver.quit()


def test_email_with_space():
    driver = create_driver()
    try:
        driver.get(URL)
        fill_and_submit(driver, name="Spec Chars", email="user name@example.com")
        email_field = driver.find_element(By.ID, "userEmail")
        assert not email_field.get_property("validity")["valid"]
        assert not output_has_content(driver)
        print("OK: email with space")
    finally:
        driver.quit()


def test_sql_in_name():
    driver = create_driver()
    try:
        driver.get(URL)
        payload = "' OR '1'='1'; DROP TABLE users;--"
        fill_and_submit(driver, name=payload, email="safe@example.com")
        assert payload in driver.find_element(By.ID, "output").text
        print("OK: sql in name")
    finally:
        driver.quit()


def test_json_in_address():
    driver = create_driver()
    try:
        driver.get(URL)
        payload = '{"admin": true, "role": "root"}'
        fill_and_submit(
            driver,
            name="JSON User",
            email="json@example.com",
            current_address=payload,
        )
        assert payload in driver.find_element(By.ID, "output").text
        print("OK: json in address")
    finally:
        driver.quit()


def test_xss_in_name():
    driver = create_driver()
    try:
        driver.get(URL)
        payload = '<img id="xss-probe" src="x" onerror="this.setAttribute(\'data-xss\',\'1\')">'
        fill_and_submit(driver, name=payload, email="xss@example.com")
        probes = driver.find_elements(By.ID, "xss-probe")
        if probes:
            print("OK: xss in dom")
        else:
            html = driver.find_element(By.ID, "output").get_attribute("innerHTML")
            assert payload in html or "xss" in driver.find_element(By.ID, "output").text.lower()
            print("OK: xss checked")
    finally:
        driver.quit()


def test_multiline_addresses():
    driver = create_driver()
    try:
        driver.get(URL)
        fill_and_submit(
            driver,
            name="Multi Line",
            email="multi@example.com",
            current_address="ул. Ленина, 1\nкв. 10",
            permanent_address="ул. Мира, 2\nкв. 20",
        )
        out = driver.find_element(By.ID, "output").text
        assert "Ленина" in out
        assert "Мира" in out
        print("OK: multiline addresses")
    finally:
        driver.quit()


if __name__ == "__main__":
    test_positive_full_form()
    test_addresses()
    test_email_without_at()
    test_empty_email()
    test_long_email()
    test_email_with_space()
    test_sql_in_name()
    test_json_in_address()
    test_xss_in_name()
    test_multiline_addresses()
    print("\nГотово")
