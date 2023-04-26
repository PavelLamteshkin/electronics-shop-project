import pytest
from src.keyboard import KeyBoard


kb = KeyBoard('logitech', 1000, 50)

# assert str(kb.language) == 'EN'

def test_change_lang():
    assert str(kb.language) == 'EN'
