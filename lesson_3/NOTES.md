# lesson_3 — homework #3

Примеры с занятия + тесты с waits / Student Registration Form.

## Примеры (examples/)

- [the_simplest_test_login.py](https://github.com/ZaharKr/qa_guru_selenium_1/blob/main/lesson_3/examples/the_simplest_test_login.py)
- [test_login.py](https://github.com/ZaharKr/qa_guru_selenium_1/blob/main/lesson_3/examples/test_login.py) — `pytest examples/test_login.py -v`
- [fluent_wait_example.py](https://github.com/ZaharKr/qa_guru_selenium_1/blob/main/lesson_3/examples/fluent_wait_example.py)
- [fluent_wait.py](https://github.com/ZaharKr/qa_guru_selenium_1/blob/main/lesson_3/examples/fluent_wait.py)
- [simple_test_student_registration_form.py](https://github.com/ZaharKr/qa_guru_selenium_1/blob/main/lesson_3/examples/simple_test_student_registration_form.py) — `python -m unittest examples.simple_test_student_registration_form`

## Свои тесты

- [test_textbox_waits.py](https://github.com/ZaharKr/qa_guru_selenium_1/blob/main/lesson_3/test_textbox_waits.py)
- [test_login_waits.py](https://github.com/ZaharKr/qa_guru_selenium_1/blob/main/lesson_3/test_login_waits.py)
- [test_student_registration_form.py](https://github.com/ZaharKr/qa_guru_selenium_1/blob/main/lesson_3/test_student_registration_form.py)

## Запуск

```bash
cd lesson_3
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

python examples/the_simplest_test_login.py
pytest examples/test_login.py -v
python examples/fluent_wait_example.py
python examples/fluent_wait.py
python -m unittest examples.simple_test_student_registration_form

python test_textbox_waits.py
python test_login_waits.py
python test_student_registration_form.py
```
