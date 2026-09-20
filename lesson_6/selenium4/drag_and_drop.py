from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

# HTML5 DnD на the-internet часто не срабатывает через ActionChains —
# поэтому после попытки Selenium делаем надёжный fallback через JS.
_JS_DND = """
var source = arguments[0], target = arguments[1];
var dataTransfer = {
  dropEffect: '', effectAllowed: 'all', files: [], items: {}, types: [],
  setData: function() {}, getData: function() {}, clearData: function() {},
  setDragImage: function() {}
};
['dragstart', 'drag', 'dragenter', 'dragover', 'drop', 'dragend'].forEach(function(type) {
  var event = document.createEvent('Event');
  event.initEvent(type, true, true);
  event.dataTransfer = dataTransfer;
  ((type === 'dragenter' || type === 'dragover' || type === 'drop') ? target : source)
    .dispatchEvent(event);
});
"""


def main():
    opts = Options()
    opts.add_argument("--headless=new")
    opts.add_argument("--window-size=1280,900")
    driver = webdriver.Chrome(options=opts)

    try:
        driver.get("https://the-internet.herokuapp.com/drag_and_drop")

        source = driver.find_element(By.ID, "column-a")
        target = driver.find_element(By.ID, "column-b")

        assert source.find_element(By.TAG_NAME, "header").text == "A"
        assert target.find_element(By.TAG_NAME, "header").text == "B"

        ActionChains(driver).drag_and_drop(source, target).perform()

        if source.find_element(By.TAG_NAME, "header").text == "A":
            driver.execute_script(_JS_DND, source, target)

        assert source.find_element(By.TAG_NAME, "header").text == "B"
        assert target.find_element(By.TAG_NAME, "header").text == "A"
        print("OK: drag_and_drop")
    finally:
        driver.quit()


if __name__ == "__main__":
    main()
