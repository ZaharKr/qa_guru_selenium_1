import sys
from pathlib import Path

import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# страницы берём из lesson_8, без копирования
sys.path.insert(0, str(Path(__file__).resolve().parents[1].parent / "lesson_8"))


@pytest.fixture
def driver():
    opts = Options()
    opts.add_argument("--headless=new")
    opts.add_argument("--window-size=1400,1000")
    browser = webdriver.Chrome(options=opts)
    yield browser
    if hasattr(browser, "get_screenshot_as_png"):
        try:
            allure.attach(
                browser.get_screenshot_as_png(),
                name="final_screenshot",
                attachment_type=allure.attachment_type.PNG,
            )
        except Exception:
            pass
    browser.quit()


@pytest.fixture
def base_url():
    return "https://qa-guru.github.io/one-page-form"


@pytest.fixture
def text_box_page(driver, base_url):
    from pages.text_box_page import TextBoxPage

    page = TextBoxPage(driver, base_url)
    with allure.step("Open Text Box"):
        page.open()
    return page


@pytest.fixture
def login_page(driver, base_url):
    from pages.login_page import LoginPage

    page = LoginPage(driver, base_url)
    with allure.step("Open Login"):
        page.open()
    return page
