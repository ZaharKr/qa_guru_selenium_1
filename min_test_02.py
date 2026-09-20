import time

from chrome_setup import PAUSE, URL, create_driver

driver = create_driver()
driver.get(URL)
driver.maximize_window()
time.sleep(PAUSE)
print("Тест успешно пройден!")
driver.quit()
