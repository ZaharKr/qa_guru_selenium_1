import pytest
from pytest_bdd import scenarios, given, when, then, parsers

# Здесь мы связываем текст из .feature файла с кодом на Python с помощью декораторов given, when, then и фикстур
# scenarios(...) — автоматически находит и регистрирует все сценарии из указанного .feature файла в качестве тестов
# Pytest.parsers.parse(...) — модуль парсинга, который позволяет вытаскивать переменные (в нашем примере {price:d} как целое число) из текста Gherkin
# передавать их в аргументы Python-функций.
# Фикстуры Pytest (basket) — используются для передачи состояния между шагами Given -> When -> Then без создания дополнительных глобальных контекстных объектов.

# Загружаем сценарии из feature-файла
scenarios('../features/basket.feature')

# Фикстура для хранения состояния корзины
@pytest.fixture
def basket():
    return {"items": [], "total": 0}

@given("пустая корзина покупателя")
def empty_basket(basket):
    basket["items"] = []
    basket["total"] = 0

@when(parsers.parse("покупатель добавляет товар стоимостью {price:d} рублей"))
def add_item_to_basket(basket, price):
    basket["items"].append(price)
    basket["total"] += price

@then(parsers.parse("итоговая стоимость корзины должна быть равна {expected_total:d} рублей"))
def verify_basket_total(basket, expected_total):
    print(basket)
    print(expected_total)
    assert basket["total"] == expected_total

# pytest -vvs