import pytest
from pytest_bdd import given, parsers, scenarios, then, when

scenarios("features/basket.feature")


@pytest.fixture
def basket():
    return {"items": [], "total": 0}


@given("пустая корзина")
def empty_basket(basket):
    basket["items"] = []
    basket["total"] = 0
    print("корзина очищена")


@when(parsers.parse("добавляю товар за {price:d}"))
def add_item(basket, price):
    basket["items"].append(price)
    basket["total"] += price
    print(f"добавлен товар {price}, total={basket['total']}")


@then(parsers.parse("итоговая сумма равна {expected:d}"))
def check_total(basket, expected):
    assert basket["total"] == expected
