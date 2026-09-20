# lesson_7 — Pytest #1

Selenium Text Box + Login на pytest (POM + fixtures).
Ориентир: https://github.com/KatjaPopova/qa_guru_homework_pytest1

## Теория
- **UT** — проверка маленьких кусков (функция/класс) изолированно
- **TDD** — red → green → refactor
- **Test Pyramid** — много unit, меньше integration, ещё меньше UI/E2E
- **Dependency Inversion** — зависеть от абстракций, не от конкретных классов
- **Dependency Injection** — зависимости снаружи (конструктор / setter / fixture); см. `di_example.py`
- **Mocking** — подмена зависимостей (`Mock`, `monkeypatch`)
- **Ортогональность** — независимые части: меняешь одну, другие не ломаются

## Pytest в проекте
- `pytest.ini` — markers, addopts, log_cli, testpaths, pythonpath
- CLI: `--headless`, `--base-url`
- fixtures: session/function, autouse log, page fixtures (DI)
- indirect parametrize + ids
- markers: smoke / regression / login / textbox / unit
- skip / skipif / xfail
- raises, approx, monkeypatch, tmp_path, caplog, capsys

## Запуск
```bash
cd lesson_7
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt

pytest
pytest -m unit
pytest -m smoke
pytest --headless=true --base-url=https://qa-guru.github.io/one-page-form -k text_box
pytest -m "login and regression" -v
```
