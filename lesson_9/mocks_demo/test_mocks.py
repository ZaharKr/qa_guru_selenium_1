from unittest.mock import MagicMock, patch

import pytest


class PaymentGateway:
    def charge(self, amount: int) -> bool:
        raise NotImplementedError("реальный платёж не вызываем в тестах")


class OrderService:
    def __init__(self, gateway: PaymentGateway):
        self.gateway = gateway

    def checkout(self, amount: int) -> str:
        print(f"checkout amount={amount}")
        ok = self.gateway.charge(amount)
        return "paid" if ok else "failed"


def test_checkout_with_unittest_mock():
    gateway = MagicMock(spec=PaymentGateway)
    gateway.charge.return_value = True
    service = OrderService(gateway)
    assert service.checkout(100) == "paid"
    gateway.charge.assert_called_once_with(100)


def test_checkout_failed_with_mocker(mocker):
    gateway = mocker.Mock(spec=PaymentGateway)
    gateway.charge.return_value = False
    service = OrderService(gateway)
    assert service.checkout(50) == "failed"


@patch.object(PaymentGateway, "charge", return_value=True)
def test_checkout_patch(mock_charge):
    service = OrderService(PaymentGateway())
    assert service.checkout(10) == "paid"
    mock_charge.assert_called_once_with(10)
