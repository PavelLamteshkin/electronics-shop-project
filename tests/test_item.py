import pytest
from src.item import Item

item = Item("Ноутбук", 100000, 5)
assert isinstance(item, Item)


@pytest.fixture
def item1():
    return Item("Наушники", 1000, 10)


def test_calculate_total_price(item1):
    assert Item.calculate_total_price(item1) == 10000


def test_apply_discount(item1):
    assert Item.apply_discount(item1) == 1000


def test_string_to_number():
    assert Item.string_to_number('7.5') == 7
    assert Item.string_to_number('7') == 7


# def test_name():
#     item2 = Item("Супернаушники", 1000, 10)
#     assert Item.name(item2.name) == 'Длина наименования товара превышает 10 символов'


def test_instantiate_from_csv():
    assert Item.instantiate_from_csv() == None

