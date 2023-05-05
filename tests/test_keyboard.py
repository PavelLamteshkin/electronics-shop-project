import pytest
from src.keyboard import KeyBoard

kb = KeyBoard('logitech', 1000, 50)
kb1 = KeyBoard('Dell', 2000, 150, 'RU')

def test_change_lang():
    assert str(kb.language) == 'EN'
    assert str(kb.change_lang().language) == 'RU'
    assert str(kb.change_lang().change_lang().language) == 'RU'

    assert str(kb1.language) == 'RU'
    assert str(kb1.change_lang().language) == 'EN'
    assert str(kb1.change_lang().change_lang().language) == 'EN'
