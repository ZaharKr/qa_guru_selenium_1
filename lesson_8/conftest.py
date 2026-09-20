import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        default="chrome",
        choices=("chrome", "firefox"),
        help="browser to use",
    )
    parser.addoption(
        "--headless",
        default="true",
        help="true/false headless mode",
    )
    parser.addoption(
        "--window-size",
        default="1400x1000",
        choices=("1920x1080", "1400x1000", "1280x720", "390x844"),
        help="browser window size WxH",
    )
    parser.addoption(
        "--base-url",
        default="https://qa-guru.github.io/one-page-form",
        help="base URL of AUT",
    )


@pytest.fixture(scope="session")
def base_url(pytestconfig):
    return pytestconfig.getoption("--base-url").rstrip("/")


@pytest.fixture
def browser_name(pytestconfig):
    return pytestconfig.getoption("--browser")


@pytest.fixture
def headless(pytestconfig):
    return pytestconfig.getoption("--headless").lower() in {"1", "true", "yes"}


@pytest.fixture
def window_size(pytestconfig):
    raw = pytestconfig.getoption("--window-size")
    w, h = raw.lower().split("x")
    return int(w), int(h)


@pytest.fixture
def driver(browser_name, headless, window_size):
    width, height = window_size
    if browser_name == "firefox":
        opts = FirefoxOptions()
        if headless:
            opts.add_argument("-headless")
        browser = webdriver.Firefox(options=opts)
    else:
        opts = ChromeOptions()
        if headless:
            opts.add_argument("--headless=new")
        opts.add_argument(f"--window-size={width},{height}")
        browser = webdriver.Chrome(options=opts)

    browser.set_window_size(width, height)
    yield browser
    browser.quit()


@pytest.fixture
def text_box_page(driver, base_url):
    from pages.text_box_page import TextBoxPage

    return TextBoxPage(driver, base_url).open()


@pytest.fixture
def login_page(driver, base_url):
    from pages.login_page import LoginPage

    return LoginPage(driver, base_url).open()


@pytest.fixture
def registration_page(driver, base_url):
    from pages.registration_page import RegistrationPage

    return RegistrationPage(driver, base_url).open()
