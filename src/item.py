import csv
import os.path

class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        self.all.append(self)


    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"


    def __str__(self):
        return f'{self.__name}'


    @property
    def name(self):
        return self.__name


    @name.setter
    def name(self, name):
        if len(name) > 10:
            raise Exception('Длина наименования товара превышает 10 символов')
        else:
            self.__name = name


    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.
        """
        return self.quantity * self.price


    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate


    @classmethod
    def instantiate_from_csv(cls):
        """
        метод инициализирующий экземпляры класса Item данными из файла src/items.csv
        """
        # path = os.path.abspath('items.csv')
        # print(os.path.isdir(r'C:\Users\MummyHouse\PycharmProjects\electronics-shop-project\src\items.csv'))
        cls.all = []
        path = r'..\src\items.csv'
        with open(path) as csvfile:
            reader = csv.DictReader(csvfile, delimiter = ',')
            for row in reader:
                name = row['name']
                price = row['price']
                quantity = row['quantity']
                item = cls(name, price, quantity)

        return cls.all


    @staticmethod
    def string_to_number(num: str):
        """
        метод возвращающий число из числа-строки
        """
        return round(int(float(num)))

# item1 = Item("Смартфон", 10000, 20)
# print(item1)
