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

## Запуск

```bash
cd lesson_3
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
pytest examples/test_login.py -v
python -m unittest examples.simple_test_student_registration_form
python test_student_registration_form.py
```
