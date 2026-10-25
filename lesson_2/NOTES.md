# lesson_2 — homework 2.1 (Text Box + Login)

Страницы:
- https://qa-guru.github.io/one-page-form/text-box.html
- https://qa-guru.github.io/one-page-form/login.html

Валидный логин: `user1` / `password1`

## Что относится к уроку 2

### examples/ — пример с занятия
- [examples/the_simplest_test_login_06.py](examples/the_simplest_test_login_06.py)

### своя работа
- [test_login_form.py](test_login_form.py) — сценарии Login Form (успех / ошибки / logout)
- [refactored_test_form_05.py](refactored_test_form_05.py) — рефакторинг Text Box в класс
- [chrome_setup.py](chrome_setup.py) — общий драйвер/хелперы для этих тестов

Файлы из урока 1 (`min_test_02`, `test_form_03`, …) здесь не дублируются — они в [lesson_1](../lesson_1).

## Запуск
```bash
cd lesson_2
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt

python examples/the_simplest_test_login_06.py
python test_login_form.py
python refactored_test_form_05.py
```
