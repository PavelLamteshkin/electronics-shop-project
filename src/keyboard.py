from src.item import Item


class MixinLang:

    language = 'RU'

    def change_lang(self):
        self.language = 'RU'
        return self


class KeyBoard(Item, MixinLang):

    def __init__(self, name: str, price: float, quantity: int):
        super().__init__(name, price, quantity)
        self.language = 'EN'
