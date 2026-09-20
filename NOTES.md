# Selenium 1 / homework 2.1

Страницы:
- https://qa-guru.github.io/one-page-form/text-box.html
- https://qa-guru.github.io/one-page-form/login.html

## DevTools
text-box: userName, userEmail, currentAddress, permanentAddress, submit, output
login: login-input, password-input, submit-button, error-message, success-panel
валидный логин: user1 / password1

## Запуск
```bash
source .venv/bin/activate
pip install -r requirements.txt

python min_test_02.py
python test_form_03.py
python r_test_form_04.py
python the_simplest_test_login_06.py
python test_form_scenarios.py
python test_login_form.py
python refactored_test_form_05.py
```

## Заметки
Работает, но править неудобно: много копипасты, браузер поднимается в каждом тесте,
данные захардкожены. Рефакторинг в класс чуть лучше, но всё равно далеко до удобного
расширения (нужны фикстуры / page object).
