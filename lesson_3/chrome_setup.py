from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

TEXT_BOX_URL = "https://qa-guru.github.io/one-page-form/text-box.html"
LOGIN_URL = "https://qa-guru.github.io/one-page-form/login.html"
REG_URL = "https://qa-guru.github.io/one-page-form/automation-practice-form.html"


def create_driver(headless=True):
    opts = Options()
    if headless:
        opts.add_argument("--headless=new")
    opts.add_argument("--window-size=1400,1000")
    opts.add_argument("--disable-gpu")
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=opts)
    driver.implicitly_wait(3)
    return driver


def wait(driver, timeout=10):
    return WebDriverWait(driver, timeout)


def js_click(driver, element):
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
    driver.execute_script("arguments[0].click();", element)


def hide_overlays(driver):
    driver.execute_script("""
        const ban = document.getElementById('fixedban');
        if (ban) ban.remove();
        const footers = document.getElementsByTagName('footer');
        if (footers.length) footers[0].style.display = 'none';
    """)
