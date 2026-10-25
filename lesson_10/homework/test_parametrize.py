"""
Подход 2: переопределяем параметр через indirect на уровне теста.
На desktop-тест идут только desktop-размеры, на mobile — только mobile.
"""

import pytest

from github_helpers import (
    DESKTOP_SIZES,
    MOBILE_SIZES,
    click_sign_in_desktop,
    click_sign_in_mobile,
    create_chrome,
    open_github,
)


@pytest.fixture
def browser(request):
    width, height = request.param
    driver = create_chrome(width, height)
    yield driver, width, height
    driver.quit()


@pytest.mark.parametrize(
    "browser",
    DESKTOP_SIZES,
    indirect=True,
    ids=[f"{w}x{h}" for w, h in DESKTOP_SIZES],
)
def test_github_desktop(browser):
    driver, width, height = browser
    wait = open_github(driver)
    click_sign_in_desktop(driver, wait)
    assert "login" in driver.current_url


@pytest.mark.parametrize(
    "browser",
    MOBILE_SIZES,
    indirect=True,
    ids=[f"{w}x{h}" for w, h in MOBILE_SIZES],
)
def test_github_mobile(browser):
    driver, width, height = browser
    wait = open_github(driver)
    click_sign_in_mobile(driver, wait)
    assert "login" in driver.current_url
