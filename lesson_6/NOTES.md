# lesson_6 — homework 4.1 (Special cases + PageFactory extended)

## 1. Продолжение ДР #3 / #5
POM уже в [lesson_5](../lesson_5). TextBox PageFactory и Fluent Interface — там же.

## 2. Selenium 4 — доп. возможности
`selenium4/`:
- `drag_and_drop.py` — ActionChains + JS fallback (HTML5 DnD)
- `add_remove_elements.py` — add/delete + assert count
- `relative_locator.py` — below / above / near / toLeftOf / toRightOf

Сайт для практики: https://the-internet.herokuapp.com/

## 3. selenium-page-factory
- TextBox PF: [../lesson_5/TextBoxPageObjectWithPageFactory](../lesson_5/TextBoxPageObjectWithPageFactory)
- Extended: `page_factory_extended_example/` — `fill_form()`, parametrize, методы wrapper:
  `set_text`, `clear_text`, `click_button`, `get_text`, `scroll_into_view`,
  `visibility_of_element_located`, `hover`, `select_element_by_value`, `getAttribute`, `is_Enabled`

Теория:
- https://pypi.org/project/selenium-page-factory/
- https://selenium-page-factory.readthedocs.io/en/latest/

## 4. Fluent Interface
- `fluent_interface/Fluent Interface Description.py`
- Реализация в [text_box_page.py](../lesson_5/TextBoxPageObject/text_box_page.py) — `return self`
- Цепочка в тестах: `.open().fill_form(...).submit().get_output_data()`

## PO vs PageFactory (сравнение)
Классический PO: явные `find_element`, падения — NoSuchElement / assert.
PageFactory: lazy-init + visibility wait → часто `ElementNotVisibleException` /
timeout на `output`, если смотреть элемент через wrapper до появления `has-content`.
Поэтому в TextBox PF для output используем native `find_element` + класс `has-content`.

## Запуск
```bash
cd lesson_6
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt

python selenium4/drag_and_drop.py
python selenium4/add_remove_elements.py
python selenium4/relative_locator.py
pytest page_factory_extended_example/test_student_registration_form_with_pf.py -v
```
