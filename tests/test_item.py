"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item

product = Item("saw", 15.0, 5)
product.pay_rate = 1.0


def test_calculate_total_price():
    assert product.calculate_total_price() == 75.0


def test_apply_discount():
    assert product.apply_discount() == 75.0
