# lesson_10 — Pytest: GitHub desktop / mobile (параметризация)

Официальное ДЗ: https://github.com/qa-guru/qa_guru_python_5_15  
Доки: https://docs.pytest.org/en/7.1.x/how-to/parametrize.html  
Wiki: https://github.com/qa-guru/knowledge-base/wiki/13.-Pytest

## Подходы

| Файл | Подход |
|------|--------|
| [homework/test_skip.py](homework/test_skip.py) | skip по соотношению сторон |
| [homework/test_parametrize.py](homework/test_parametrize.py) | indirect-параметризация |
| [homework/test_fixtures.py](homework/test_fixtures.py) | разные фикстуры |

Примеры с занятия: [examples/](examples/)

## Плюсы / минусы

### 1. skip внутри теста
- **+** один набор размеров в фикстуре, легко добавить новый размер
- **+** видно в отчёте, что кейс «не подходит» (skipped)
- **−** лишние запуски браузера до skip (если skip после создания driver)
- **−** легко забыть skip и получить ложный fail

### 2. indirect
- **+** на тест идут только нужные размеры — без лишних skip
- **+** явно: `@parametrize(..., indirect=True)`
- **−** чуть сложнее читать (параметр → фикстура)
- **−** список размеров дублируется на каждом тесте

### 3. разные фикстуры
- **+** самый простой и очевидный код
- **+** нет «чужих» размеров вообще
- **−** дублирование setup (две фикстуры)
- **−** хуже масштабируется, если размеров много

## Запуск
```bash
cd lesson_10
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
pytest homework -v
```
