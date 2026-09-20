# Selenium 1

Страница: https://qa-guru.github.io/one-page-form/text-box.html

## Локаторы (смотрел в DevTools)
- userName
- userEmail
- currentAddress
- permanentAddress
- submit
- output

Email с type=email, поэтому без @ браузер сам не даёт отправить форму.
В output данные вставляются через innerHTML.

## Запуск
```bash
source .venv/bin/activate
pip install -r requirements.txt
python min_test_02.py
python test_form_03.py
python r_test_form_04.py
python test_form_scenarios.py
```

## Заметки
Код с занятия работает, но копипаста бесит — каждый тест заново открывает браузер
и ищет одни и те же поля. Данные прямо в send_keys, менять неудобно.
