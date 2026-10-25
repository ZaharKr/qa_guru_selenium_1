# test_math_utils.py
import pytest
from math_utils import divide

def test_divide_success():
    assert divide(10, 2) == 5.0

# Если бы мы написали только test_divide_success, то строка с raise ValueError не выполнилась бы,
# и pytest-cov показал бы неполный процент покрытия (Cover) и номер пропущенной строки в графе Missing
def test_divide_by_zero():
    with pytest.raises(ValueError, match="Деление на ноль"):
        divide(5, 0)

# pip install pytest pytest-cov
# pytest --cov=math_utils --cov-report=term-missing
# --cov=math_utils — измерять покрытие для модуля math_utils
# --cov-report=term-missing — вывести красивую табличку в терминал с указанием номеров строк, которые тесты «забыли» проверить.
