"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest

from src.item import Item

@pytest.fixture
def instance_item():
    return Item("Смартфон", 10000, 20)

def test_calculate_total_price(instance_item):
    assert instance_item.calculate_total_price() == 200000

def test_apply_discount(instance_item):
    instance_item.pay_rate = 0.8
    instance_item.apply_discount()
    assert instance_item.price == 8000.0

def test_name(instance_item):
    assert instance_item.name == 'Смартфон'
    instance_item.name = 'СуперСмартфон'
    assert instance_item.name == 'Exception: Длина наименования товара превышает 10 символов.'

def test_string_to_number(instance_item):
    assert instance_item.string_to_number('123') == 123
    assert instance_item.string_to_number('123.1') == 123

def test_repr(instance_item):
    assert instance_item.__repr__() == "Item('Смартфон', 10000, 20)"

def test_str(instance_item):
    assert instance_item.__str__() == 'Смартфон'