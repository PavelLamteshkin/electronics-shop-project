from src.item import Item


class MixinLang:

    def change_lang(self):
        if self.language == 'EN':
            self.language = 'RU'
        elif self.language == 'RU':
            self.language = 'EN'
        return self


class KeyBoard(Item, MixinLang):

    def __init__(self, name: str, price: float, quantity: int, language='EN'):
        super().__init__(name, price, quantity)
        self.language = language
