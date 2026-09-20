from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from seleniumpagefactory.Pagefactory import PageFactory


class TableElement:
    def __init__(self, driver, locator):
        self.driver = driver
        self.locator = locator

    @property
    def element(self):
        return self.driver.find_element(*self.locator)

    def get_headers(self) -> list[str]:
        header_elements = self.element.find_elements(By.CSS_SELECTOR, "thead th")
        return [header.text for header in header_elements]

    def get_row_data(self, row_index: int) -> list[str]:
        rows = self.element.find_elements(By.CSS_SELECTOR, "tbody tr")
        cells = rows[row_index].find_elements(By.TAG_NAME, "td")
        return [cell.text for cell in cells]

    def get_cell_value(self, row_index: int, column_index: int) -> str:
        return self.get_row_data(row_index)[column_index]


class TablesPage(PageFactory):
    def __init__(self, driver):
        self.driver = driver
        self.locators = {
            "table1": ("ID", "table1"),
            "table2": ("ID", "table2"),
        }

    def open(self):
        self.driver.get("https://the-internet.herokuapp.com/tables")
        return self

    def table(self, which: str) -> TableElement:
        locator = (By.ID, "table1" if which == "1" else "table2")
        return TableElement(self.driver, locator)


def test_table1():
    opts = Options()
    opts.add_argument("--headless=new")
    driver = webdriver.Chrome(options=opts)
    try:
        page = TablesPage(driver).open()
        table = page.table("1")
        headers = table.get_headers()
        first_row = table.get_row_data(0)
        cell = table.get_cell_value(2, 3)
        assert "Last Name" in headers
        assert "Smith" in first_row
        assert cell == "$100.00"
        print("OK: table1")
    finally:
        driver.quit()


def test_table2():
    opts = Options()
    opts.add_argument("--headless=new")
    driver = webdriver.Chrome(options=opts)
    try:
        page = TablesPage(driver).open()
        table = page.table("2")
        headers = table.get_headers()
        first_row = table.get_row_data(0)
        assert "Last Name" in headers
        assert "Smith" in first_row
        print("OK: table2")
    finally:
        driver.quit()


def test_both_tables():
    opts = Options()
    opts.add_argument("--headless=new")
    driver = webdriver.Chrome(options=opts)
    try:
        page = TablesPage(driver).open()
        t1 = page.table("1")
        t2 = page.table("2")
        assert t1.get_headers() == t2.get_headers()
        assert t1.get_row_data(0)[0] == t2.get_row_data(0)[0]
        assert t1.get_cell_value(1, 3) == t2.get_cell_value(1, 3)
        print("OK: both tables")
    finally:
        driver.quit()


if __name__ == "__main__":
    test_table1()
    test_table2()
    test_both_tables()
