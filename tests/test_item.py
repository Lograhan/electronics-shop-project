"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest

from src.item import Item

product = Item("смартфон", 15.0, 5)
product.pay_rate = 1.0
product1 = Item('СуперСмартфон', 10, 3)


def test_calculate_total_price():
    assert product.calculate_total_price() == 75.0


def test_apply_discount():
    assert product.apply_discount() == 75.0


def test_item_name():
    assert product.set_name == 'смартфон'
    assert product1.string_to_number(1) == 1
    assert product1.string_to_number("5") == 5
    with pytest.raises(Exception):
        product1.set_name