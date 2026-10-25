"""Простая «бизнес-логика» на print — без Selenium, для отчёта Allure."""


def create_order(product: str, price: int) -> dict:
    print(f"[logic] создаём заказ: {product} за {price}")
    return {"product": product, "price": price, "status": "new"}


def pay_order(order: dict, amount: int) -> dict:
    print(f"[logic] оплата заказа {order['product']}: {amount}")
    if amount < order["price"]:
        print("[logic] недостаточно средств")
        order["status"] = "failed"
        return order
    order["status"] = "paid"
    print("[logic] заказ оплачен")
    return order


def cancel_order(order: dict) -> dict:
    print(f"[logic] отмена заказа {order['product']}")
    order["status"] = "cancelled"
    return order
