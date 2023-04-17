import pytest
from src.phone import Phone


phone1 = Phone("iPhone", 100_000, 10, 2)


def test_init():
    assert phone1.number_of_sim == 2


def test_repr():
    assert repr(phone1) == "Phone('iPhone', 100000, 10, 2)"


def test_str():
    assert str(phone1) == "iPhone"
