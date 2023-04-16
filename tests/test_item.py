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
    assert item1.price == 1000
    assert Item.pay_rate == 1.0
    Item.pay_rate = 0.5
    item1.apply_discount()
    assert item1.price == 500.0


def test_string_to_number():
    assert Item.string_to_number('7.5') == 7
    assert Item.string_to_number('7') == 7


def test_name():
    item2 = Item("Наушники", 1000, 10)
    with pytest.raises(Exception):
        item2.name = "Супернаушники"


def test_instantiate_from_csv():
    assert len(Item.instantiate_from_csv()) == 5


def test___str__():
    item1 = Item("Смартфон", 10000, 20)
    assert str(item1) == "Смартфон"


def test___repr__():
    item1 = Item("Смартфон", 10000, 20)
    assert repr(item1) == "Item('Смартфон', 10000, 20)"
