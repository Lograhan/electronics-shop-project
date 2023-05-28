"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest

from src.item import Item
from src.phone import Phone

product = Item('Смартфон', 15, 5)
product.pay_rate = 1.0
product1 = Item('СуперСмартфон', 10, 3)


def test_calculate_total_price():
    assert product.calculate_total_price() == 75


def test_apply_discount():
    assert product.apply_discount() == 15.0


def test_item_name():
    assert product.name == 'Смартфон'
    assert product1.string_to_number(1) == 1
    assert product1.string_to_number("5") == 5
    with pytest.raises(Exception):
        product1.set_name


def test_repr_str():
    assert repr(product) == "Item('Смартфон', 15.0, 5)"
    assert str(product) == 'Смартфон'

def test_add():
    item1 = Item("Смартфон", 10000, 20)
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    assert item1 + phone1 == 25
    assert phone1 + phone1 == 10
    with pytest.raises(ValueError):
        phone1 + 10
    with pytest.raises(ValueError):
        item1 + 10