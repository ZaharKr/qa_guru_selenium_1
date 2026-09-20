from selene import browser, have

# https://github.com/yashaka/selene

# "selene ImportError: cannot import name 'AnyDevice' from 'selenium.webdriver.common.action_chains'"
# selene 2.0.0rc9 была выпущена в марте 2024 года. В тот период Selenium еще не использовал внутренний тип AnyDevice в своем модуле action_chains.
# selenium 4.44.0 была выпущена в мае 2026 года. В этой современной версии разработчики Selenium обновили аннотации типов и добавили AnyDevice, сломав обратную совместимость со старыми релиз-кандидатами Selene.
# Решение: понизить версию Selenium под вашу текущую Selene (на виртуальном env)
# pip install "selenium>=4.12.0,<4.17.0"

# 1. Создание виртуального окружения
#python -m venv venv

# 1.5 Если не отработал пункт 2 под Windows
# PowerShell: Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

# 2. Активация (Для Windows)
#venv\Scripts\activate
# 2. Активация (Для macOS/Linux)
#source venv/bin/activate

# 3. Правильное решение для большинства случаев:
# pip install selenium
# pip install selene
# pip install "selenium>=4.12.0,<4.17.0"
# pip install --force-reinstall selene==2.0.0rc9 --pre
# pip show selene selenium

# Мой путь :) с зацикливанием проблемы
# 3. Установка соотв версии Selenium и Selene
# pip install "selenium>=4.12.0,<4.17.0"
# pip install selene # почему-то устанавливает устаревшую версию и появляются новые проблемы
# 4. Убедиться что установлены нужные версии (версия selene очень устаревшая)
# pip show selene selenium 
# 5. pip install --force-reinstall selene==2.0.0rc9 --pre # эта команда к сожалению зацикливает проблему
# 6. pip install "selenium>=4.12.0,<4.17.0" # Проблема решена

def test_google_search():
    # 1. Открываем главную страницу Google
    browser.open('https://google.com')

    # 2. Находим поле поиска, вводим текст и нажимаем Enter
    browser.element('[name="q"]').type('selene python').press_enter()

    # 3. Проверяем, что на странице результатов есть ссылка на GitHub
    browser.element('#search').should(have.text('yashaka/selene'))

test_google_search()

