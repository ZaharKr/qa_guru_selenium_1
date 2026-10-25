from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

# десктоп = ширина > высоты (landscape), мобильный = наоборот (portrait)
DESKTOP_SIZES = [(1920, 1080), (1366, 768), (1280, 720)]
MOBILE_SIZES = [(390, 844), (360, 800), (414, 896)]
ALL_SIZES = DESKTOP_SIZES + MOBILE_SIZES


def is_desktop(width: int, height: int) -> bool:
    return width > height


def create_chrome(width: int, height: int):
    opts = Options()
    opts.add_argument("--headless=new")
    opts.add_argument(f"--window-size={width},{height}")
    opts.add_argument("--disable-gpu")
    driver = webdriver.Chrome(options=opts)
    driver.set_window_size(width, height)
    return driver


def open_github(driver):
    driver.get("https://github.com/")
    return WebDriverWait(driver, 15)


def click_sign_in_desktop(driver, wait):
    # десктоп: ссылка Sign in в шапке
    link = wait.until(ec.element_to_be_clickable((By.LINK_TEXT, "Sign in")))
    link.click()
    wait.until(ec.url_contains("login"))


def click_sign_in_mobile(driver, wait):
    # мобильный: сначала меню, потом Sign in
    menu = wait.until(
        ec.element_to_be_clickable(
            (By.CSS_SELECTOR, "button[aria-label='Toggle navigation']")
        )
    )
    menu.click()
    link = wait.until(ec.element_to_be_clickable((By.LINK_TEXT, "Sign in")))
    link.click()
    wait.until(ec.url_contains("login"))
