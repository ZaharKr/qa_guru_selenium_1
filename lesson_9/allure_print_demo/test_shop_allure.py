import json
import logging
import sys

import allure
import pytest

from shop import cancel_order, create_order, pay_order

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


@allure.epic("Интернет-магазин")
@allure.feature("Заказы")
class TestOrders:
    @allure.story("Успешная покупка")
    @allure.title("Создание и оплата заказа")
    @allure.description("Сценарий: создать заказ → оплатить полной суммой")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.tag("smoke", "orders")
    @allure.label("owner", "ZaharKr")
    @allure.testcase("https://qa-guru.github.io/", "TMS-ORD-1")
    def test_successful_purchase(self):
        with allure.step("Создаём заказ"):
            order = create_order("Notebook", 1000)
            allure.attach(
                json.dumps(order, ensure_ascii=False, indent=2),
                name="order.json",
                attachment_type=allure.attachment_type.JSON,
            )
        with allure.step("Оплачиваем заказ"):
            paid = pay_order(order, 1000)
        with allure.step("Проверяем статус paid"):
            assert paid["status"] == "paid"

    @allure.story("Негативные сценарии")
    @allure.title("Недостаточно средств")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.issue("SHOP-42", "Недостаточно средств")
    def test_not_enough_money(self):
        with allure.step("Создаём дорогой заказ"):
            order = create_order("Phone", 5000)
        with allure.step("Пытаемся оплатить меньшей суммой"):
            result = pay_order(order, 100)
            allure.attach(
                f"status={result['status']}",
                name="pay_result",
                attachment_type=allure.attachment_type.TEXT,
            )
        assert result["status"] == "failed"

    @allure.story("Отмена")
    @allure.title("Отмена нового заказа")
    def test_cancel(self):
        order = create_order("Book", 200)
        cancelled = cancel_order(order)
        assert cancelled["status"] == "cancelled"


@allure.feature("Параметризация + Allure")
@allure.story("Сложение цен")
@pytest.mark.parametrize(
    "a, b, expected",
    [(100, 200, 300), (50, 50, 100), (0, 10, 10)],
    ids=["100+200", "50+50", "0+10"],
)
def test_sum_prices(a, b, expected):
    with allure.step(f"Считаем {a} + {b}"):
        print(f"sum {a}+{b}")
        result = a + b
    allure.dynamic.parameter("a", a)
    allure.dynamic.parameter("b", b)
    assert result == expected


@allure.feature("Вложения и логи")
def test_attachments_and_logs():
    logger.info("INFO через logging")
    print("stdout message")
    print("stderr message", file=sys.stderr)
    allure.attach("<h1>Allure HTML</h1>", name="html", attachment_type=allure.attachment_type.HTML)
    allure.attach("<root>ok</root>", name="xml", attachment_type=allure.attachment_type.XML)
    assert True


def test_dynamic_labels():
    allure.dynamic.epic("Интернет-магазин")
    allure.dynamic.feature("Динамические метки")
    allure.dynamic.story("dynamic API")
    allure.dynamic.severity(allure.severity_level.MINOR)
    allure.dynamic.tag("dynamic")
    allure.dynamic.link("https://allurereport.org/", name="Allure docs")
    print("dynamic labels applied")
    assert True


@pytest.fixture
def make_order():
    created = []

    def _factory(product: str, price: int):
        order = create_order(product, price)
        created.append(order)
        return order

    yield _factory
    for order in created:
        print(f"[teardown] cleanup {order['product']}")


@allure.feature("Fixture factory")
def test_factory_fixture(make_order):
    first = make_order("A", 10)
    second = make_order("B", 20)
    assert first["status"] == "new"
    assert second["price"] == 20
