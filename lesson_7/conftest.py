import logging

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

logger = logging.getLogger(__name__)


def pytest_addoption(parser):
    parser.addoption(
        "--headless",
        action="store",
        default="true",
        help="true/false — запуск Chrome в headless",
    )
    parser.addoption(
        "--base-url",
        action="store",
        default="https://qa-guru.github.io/one-page-form",
        help="базовый URL приложения",
    )


@pytest.fixture(scope="session")
def base_url(pytestconfig):
    return pytestconfig.getoption("--base-url").rstrip("/")


@pytest.fixture
def headless(pytestconfig):
    return pytestconfig.getoption("--headless").lower() in {"1", "true", "yes"}


@pytest.fixture
def driver(headless):
    opts = Options()
    if headless:
        opts.add_argument("--headless=new")
    opts.add_argument("--window-size=1400,1000")
    browser = webdriver.Chrome(options=opts)
    browser.implicitly_wait(3)
    yield browser
    browser.quit()


@pytest.fixture(autouse=True)
def _log_test_name(request):
    logger.info("START %s", request.node.nodeid)
    yield
    logger.info("END %s", request.node.nodeid)


@pytest.fixture
def text_box_page(driver, base_url):
    from pages.text_box_page import TextBoxPage

    page = TextBoxPage(driver, base_url)
    page.open()
    return page


@pytest.fixture
def login_page(driver, base_url):
    from pages.login_page import LoginPage

    page = LoginPage(driver, base_url)
    page.open()
    return page
