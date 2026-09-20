from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

TEXT_BOX_URL = "https://qa-guru.github.io/one-page-form/text-box.html"
LOGIN_URL = "https://qa-guru.github.io/one-page-form/login.html"
URL = TEXT_BOX_URL
PAUSE = 1


def create_driver(headless=True):
    opts = Options()
    if headless:
        opts.add_argument("--headless=new")
    opts.add_argument("--window-size=1280,900")
    opts.add_argument("--disable-gpu")
    service = Service(ChromeDriverManager().install())
    return webdriver.Chrome(service=service, options=opts)


def click_element(driver, element):
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
    time.sleep(0.3)
    try:
        element.click()
    except Exception:
        driver.execute_script("arguments[0].click();", element)


def click_submit(driver):
    click_element(driver, driver.find_element(By.ID, "submit"))


def click_login_submit(driver):
    click_element(driver, driver.find_element(By.ID, "submit-button"))
