# lesson_9 — Pytest #3 (Allure + BDD / unittest / mocks)

Теория: https://github.com/qa-guru/knowledge-base/wiki/9.-Allure-Reports-Python

## Структура
- `examples/` — материалы с занятия (allure / bdd / cov)
- `allure_print_demo/` — ДЗ1: print-логика + возможности allure + pytest
- `selenium_allure/` — ДЗ2: Selenium + allure (страницы из lesson_8)
- `bdd_basket/` — ★ pytest-bdd
- `unittest_demo/` — ★ unittest
- `mocks_demo/` — ★ pytest-mock / unittest.mock

Также allure подключён в `lesson_7` и `lesson_8` (`--alluredir=allure-results`).

## Установка Allure (macOS)
```bash
pip install allure-pytest
brew install allure          # тянет openjdk
export PATH="/opt/homebrew/opt/openjdk/bin:$PATH"
allure --version
```

## Запуск
```bash
cd lesson_9
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt

# ДЗ1
pytest allure_print_demo -v --alluredir=allure-results
allure serve allure-results

# ДЗ2 Selenium
pytest selenium_allure -v --alluredir=allure-results

# ★
pytest bdd_basket -v
python -m unittest discover -s unittest_demo -v
pytest mocks_demo -v

# coverage (пример с занятия)
pytest examples/test_cov_the_simplest_example --cov=examples.test_cov_the_simplest_example.math_utils --cov-report=term-missing
```
