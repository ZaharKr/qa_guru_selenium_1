# lesson_5 — POM / PageFactory / PageElement

## Что внутри
- `automation_practice_form` — initial → PO, 3 теста, CalendarElement
- `TextBoxPageObject` vs `TextBoxPageObjectWithPageFactory`
- `the_simplest_page_factory` — login через PageFactory
- `calendar_page_element_with_selene` (+ selenium-версия)
- `table_page_element_example` — table1/table2 + PageFactory
- `example_from_student` — студенческий POM

## PO vs PageFactory
Классический PO: локаторы tuple + `find_element`, всё явно.
PageFactory (`selenium-page-factory`): локаторы в dict, элементы как атрибуты,
есть `set_text` / `click_button` с ожиданием. Падения могут отличаться из‑за
разной инициализации элементов и встроенных wait.

## TODO закрыты
- setup/tear_down на каждый тест + 3 набора данных
- Calendar Page Element
- `is_email_error_present` при `class is None`
- long fields без if в тесте (parametrize kwargs)
- XSS/HTML: проверка через page_source / empty text
- таблица 2 + оба сразу + PageFactory
- календарь на Selenium + закрытие баннера в Selene
- PageFactory на реальном login

## Запуск
```bash
cd lesson_5
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt

cd automation_practice_form && python automation_practice_form_test_suite.py && cd ..
cd TextBoxPageObject && pytest -v test_text_box.py && cd ..
cd TextBoxPageObjectWithPageFactory && pytest -v test_text_box_pf.py && cd ..
cd the_simplest_page_factory && python the_simplest_page_factory.py && cd ..
cd table_page_element_example && python table_page_element_example.py && cd ..
cd calendar_page_element_with_selene && python calendar_page_element_selenium.py && cd ..
```
