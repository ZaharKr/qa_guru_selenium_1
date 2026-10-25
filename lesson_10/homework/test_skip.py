"""
Подход 1: параметризация фикстуры несколькими размерами окна.
Пропускаем мобильный тест, если соотношение сторон десктопное (и наоборот).
"""

import pytest

from github_helpers import (
    ALL_SIZES,
    click_sign_in_desktop,
    click_sign_in_mobile,
    create_chrome,
    is_desktop,
    open_github,
)


@pytest.fixture(params=ALL_SIZES, ids=[f"{w}x{h}" for w, h in ALL_SIZES])
def browser(request):
    width, height = request.param
    driver = create_chrome(width, height)
    yield driver, width, height
    driver.quit()


def test_github_desktop(browser):
    driver, width, height = browser
    if not is_desktop(width, height):
        pytest.skip("мобильное соотношение сторон — этот тест только для desktop")

    wait = open_github(driver)
    click_sign_in_desktop(driver, wait)
    assert "login" in driver.current_url


def test_github_mobile(browser):
    driver, width, height = browser
    if is_desktop(width, height):
        pytest.skip("десктопное соотношение сторон — этот тест только для mobile")

    wait = open_github(driver)
    click_sign_in_mobile(driver, wait)
    assert "login" in driver.current_url
