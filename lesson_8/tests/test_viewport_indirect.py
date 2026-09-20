import pytest
from selenium.webdriver.common.by import By


DESKTOP = (1920, 1080)
MOBILE = (390, 844)


@pytest.fixture
def sized_driver(request, headless):
    """indirect: размер окна приходит из @parametrize."""
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options

    width, height = request.param
    opts = Options()
    if headless:
        opts.add_argument("--headless=new")
    opts.add_argument(f"--window-size={width},{height}")
    browser = webdriver.Chrome(options=opts)
    browser.set_window_size(width, height)
    yield browser, width, height
    browser.quit()


@pytest.mark.regression
@pytest.mark.desktop
@pytest.mark.parametrize("sized_driver", [DESKTOP], indirect=True, ids=["desktop-1920"])
def test_desktop_sign_in_visible(sized_driver):
    driver, width, height = sized_driver
    if width < 800:
        pytest.skip("мобильный viewport — другой тест")
    driver.get("https://github.com/")
    links = driver.find_elements(By.PARTIAL_LINK_TEXT, "Sign in")
    assert links, "на десктопе должна быть ссылка Sign in"


@pytest.mark.regression
@pytest.mark.mobile
@pytest.mark.parametrize("sized_driver", [MOBILE], indirect=True, ids=["mobile-390"])
def test_mobile_viewport(sized_driver):
    driver, width, height = sized_driver
    if width >= 800:
        pytest.skip("десктопный viewport — другой тест")
    driver.get("https://github.com/")
    assert driver.get_window_size()["width"] <= 500
