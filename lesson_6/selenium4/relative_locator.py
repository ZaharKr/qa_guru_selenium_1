from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with


def main():
    opts = Options()
    opts.add_argument("--headless=new")
    opts.add_argument("--window-size=1400,1000")
    driver = webdriver.Chrome(options=opts)

    try:
        # --- text-box: below / above / near ---
        driver.get("https://qa-guru.github.io/one-page-form/text-box.html")

        full_name_label = driver.find_element(By.XPATH, "//label[text()='Full Name']")
        full_name_input = driver.find_element(
            locate_with(By.TAG_NAME, "input").below(full_name_label)
        )
        full_name_input.send_keys("Ivan Ivanov")

        submit_btn = driver.find_element(By.ID, "submit")
        email_input = driver.find_element(
            locate_with(By.TAG_NAME, "input").above(submit_btn)
        )
        email_input.send_keys("ivan@example.com")

        label_element = driver.find_element(By.XPATH, "//label[text()='Current Address']")
        address_textarea = driver.find_element(
            locate_with(By.TAG_NAME, "textarea").near(label_element)
        )
        address_textarea.send_keys("г. Минск, ул. Академическая")

        # --- practice form: toLeftOf / toRightOf (радиокнопки) ---
        driver.get("https://qa-guru.github.io/one-page-form/automation-practice-form.html")

        second_radio = driver.find_element(By.ID, "gender-radio-2")
        first_radio = driver.find_element(
            locate_with(By.CSS_SELECTOR, "input[type='radio']").to_left_of(second_radio)
        )
        driver.execute_script("arguments[0].click();", first_radio)

        first_radio = driver.find_element(By.ID, "gender-radio-1")
        second_radio = driver.find_element(
            locate_with(By.CSS_SELECTOR, "input[type='radio']").to_right_of(first_radio)
        )
        driver.execute_script("arguments[0].click();", second_radio)

        print("OK: relative_locator")
    finally:
        driver.quit()


if __name__ == "__main__":
    main()
