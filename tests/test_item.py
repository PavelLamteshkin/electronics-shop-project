import pytest
from src.item import Item


@pytest.fixture
def item1():
    return Item("Наушники", 1000, 10)


def test_calculate_total_price(item1):
    assert Item.calculate_total_price(item1) == 10000


def test_apply_discount(item1):
    assert Item.apply_discount(item1) == 1000
