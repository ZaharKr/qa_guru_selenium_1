"""
Подход 3: разные фикстуры для каждого теста (свой размер окна).
"""

import pytest

from github_helpers import (
    click_sign_in_desktop,
    click_sign_in_mobile,
    create_chrome,
    open_github,
)


@pytest.fixture
def desktop_browser():
    driver = create_chrome(1920, 1080)
    yield driver
    driver.quit()


@pytest.fixture
def mobile_browser():
    driver = create_chrome(390, 844)
    yield driver
    driver.quit()


def test_github_desktop(desktop_browser):
    wait = open_github(desktop_browser)
    click_sign_in_desktop(desktop_browser, wait)
    assert "login" in desktop_browser.current_url


def test_github_mobile(mobile_browser):
    wait = open_github(mobile_browser)
    click_sign_in_mobile(mobile_browser, wait)
    assert "login" in mobile_browser.current_url
