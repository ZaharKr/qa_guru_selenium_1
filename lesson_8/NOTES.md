# lesson_8 — Pytest #2: параметризация и расширения

Ориентир: https://github.com/arb-cs/qa-guru-python-homework/tree/pytest-intro/tests  
CLI-идеи: `2/conftest_example.py` (browser / window-size / headless).

## Параметризация
- `tests/test_parametrize_examples.py` — ids, pytest.param+marks, cartesian,
  fixture params, indirect, pytest_generate_tests, dict/csv
- UI: login / textbox / registration с `@parametrize`
- `test_viewport_indirect.py` — indirect + skip desktop/mobile

## CLI
```bash
pytest --browser=chrome --headless=true --window-size=1400x1000
pytest --base-url=https://qa-guru.github.io/one-page-form -m smoke
pytest -m unit
pytest -m "registration and regression"
```

## Запуск
```bash
cd lesson_8
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
pytest
pytest -m unit
pytest -m smoke
```
