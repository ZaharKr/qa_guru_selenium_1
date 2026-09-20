# qa_guru_selenium_1

Ссылка на проект: https://github.com/ZaharKr/qa_guru_selenium_1

## lesson_1 — Text Box Form

Директория: [lesson_1](https://github.com/ZaharKr/qa_guru_selenium_1/tree/main/lesson_1)

- [min_test_02.py](https://github.com/ZaharKr/qa_guru_selenium_1/blob/main/lesson_1/min_test_02.py)
- [test_form_03.py](https://github.com/ZaharKr/qa_guru_selenium_1/blob/main/lesson_1/test_form_03.py)
- [r_test_form_04.py](https://github.com/ZaharKr/qa_guru_selenium_1/blob/main/lesson_1/r_test_form_04.py)
- [test_form_scenarios.py](https://github.com/ZaharKr/qa_guru_selenium_1/blob/main/lesson_1/test_form_scenarios.py)

## lesson_2 — homework 2.1 (Text Box + Login)

Директория: [lesson_2](https://github.com/ZaharKr/qa_guru_selenium_1/tree/main/lesson_2)

- [the_simplest_test_login_06.py](https://github.com/ZaharKr/qa_guru_selenium_1/blob/main/lesson_2/the_simplest_test_login_06.py)
- [test_login_form.py](https://github.com/ZaharKr/qa_guru_selenium_1/blob/main/lesson_2/test_login_form.py)
- [refactored_test_form_05.py](https://github.com/ZaharKr/qa_guru_selenium_1/blob/main/lesson_2/refactored_test_form_05.py)

## lesson_3 — homework #3 (waits + Student Registration Form)

Директория: [lesson_3](https://github.com/ZaharKr/qa_guru_selenium_1/tree/main/lesson_3)

Примеры с занятия:
- [examples/the_simplest_test_login.py](https://github.com/ZaharKr/qa_guru_selenium_1/blob/main/lesson_3/examples/the_simplest_test_login.py)
- [examples/test_login.py](https://github.com/ZaharKr/qa_guru_selenium_1/blob/main/lesson_3/examples/test_login.py)
- [examples/fluent_wait_example.py](https://github.com/ZaharKr/qa_guru_selenium_1/blob/main/lesson_3/examples/fluent_wait_example.py)
- [examples/simple_test_student_registration_form.py](https://github.com/ZaharKr/qa_guru_selenium_1/blob/main/lesson_3/examples/simple_test_student_registration_form.py)

Тесты:
- [test_textbox_waits.py](https://github.com/ZaharKr/qa_guru_selenium_1/blob/main/lesson_3/test_textbox_waits.py)
- [test_login_waits.py](https://github.com/ZaharKr/qa_guru_selenium_1/blob/main/lesson_3/test_login_waits.py)
- [test_student_registration_form.py](https://github.com/ZaharKr/qa_guru_selenium_1/blob/main/lesson_3/test_student_registration_form.py)

## lesson_5 — homework #5 (POM / PageFactory / PageElement)

Директория: [lesson_5](https://github.com/ZaharKr/qa_guru_selenium_1/tree/main/lesson_5)

- [automation_practice_form](https://github.com/ZaharKr/qa_guru_selenium_1/tree/main/lesson_5/automation_practice_form)
- [TextBoxPageObject](https://github.com/ZaharKr/qa_guru_selenium_1/tree/main/lesson_5/TextBoxPageObject)
- [TextBoxPageObjectWithPageFactory](https://github.com/ZaharKr/qa_guru_selenium_1/tree/main/lesson_5/TextBoxPageObjectWithPageFactory)
- [the_simplest_page_factory](https://github.com/ZaharKr/qa_guru_selenium_1/tree/main/lesson_5/the_simplest_page_factory)
- [calendar_page_element_with_selene](https://github.com/ZaharKr/qa_guru_selenium_1/tree/main/lesson_5/calendar_page_element_with_selene)
- [table_page_element_example](https://github.com/ZaharKr/qa_guru_selenium_1/tree/main/lesson_5/table_page_element_example)
- [example_from_student](https://github.com/ZaharKr/qa_guru_selenium_1/tree/main/lesson_5/example_from_student)

## lesson_6 — homework 4.1 (Special cases + PageFactory extended)

Директория: [lesson_6](https://github.com/ZaharKr/qa_guru_selenium_1/tree/main/lesson_6)

- [selenium4/drag_and_drop.py](https://github.com/ZaharKr/qa_guru_selenium_1/blob/main/lesson_6/selenium4/drag_and_drop.py)
- [selenium4/add_remove_elements.py](https://github.com/ZaharKr/qa_guru_selenium_1/blob/main/lesson_6/selenium4/add_remove_elements.py)
- [selenium4/relative_locator.py](https://github.com/ZaharKr/qa_guru_selenium_1/blob/main/lesson_6/selenium4/relative_locator.py)
- [page_factory_extended_example](https://github.com/ZaharKr/qa_guru_selenium_1/tree/main/lesson_6/page_factory_extended_example)
- [fluent_interface](https://github.com/ZaharKr/qa_guru_selenium_1/tree/main/lesson_6/fluent_interface)
- [NOTES.md](https://github.com/ZaharKr/qa_guru_selenium_1/blob/main/lesson_6/NOTES.md)

## Запуск

```bash
cd lesson_5
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python automation_practice_form/automation_practice_form_test_suite.py
pytest TextBoxPageObject/test_text_box.py -v
pytest TextBoxPageObjectWithPageFactory/test_text_box_pf.py -v
python table_page_element_example/table_page_element_example.py

cd ../lesson_6
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python selenium4/drag_and_drop.py
python selenium4/add_remove_elements.py
python selenium4/relative_locator.py
pytest page_factory_extended_example/test_student_registration_form_with_pf.py -v
```
