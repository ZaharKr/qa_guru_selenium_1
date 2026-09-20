from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


def main():
    opts = Options()
    opts.add_argument("--headless=new")
    opts.add_argument("--window-size=1280,900")
    driver = webdriver.Chrome(options=opts)

    try:
        driver.get("https://the-internet.herokuapp.com/add_remove_elements/")
        add_button = driver.find_element(By.XPATH, "//button[text()='Add Element']")

        for _ in range(3):
            add_button.click()

        delete_buttons = driver.find_elements(By.CLASS_NAME, "added-manually")
        assert len(delete_buttons) == 3

        for button in delete_buttons:
            button.click()

        remaining = driver.find_elements(By.CLASS_NAME, "added-manually")
        assert len(remaining) == 0
        print("OK: add_remove_elements")
    finally:
        driver.quit()


if __name__ == "__main__":
    main()
