import csv


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    path = r'..\src\items.csv'
    # path = r'..\src\wrong_items.csv'

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        self.all.append(self)
        super().__init__()

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

        # cls.all = []
        # path = r'..\src\items.csv'

        try:
            with open(cls.path) as csvfile:
                reader = csv.DictReader(csvfile, delimiter=',')
        except FileNotFoundError:
            print('FileNotFoundError: Отсутствует файл items.csv')
        else:
            try:
                with open(cls.path) as csvfile:
                    reader = csv.DictReader(csvfile, delimiter=',')
                    if len(reader.fieldnames) != 3:
                        raise InstantiateCSVError
            except InstantiateCSVError as a:
                print('InstantiateCSVError: Файл item.csv поврежден')
            else:
                with open(cls.path) as csvfile:
                    reader = csv.DictReader(csvfile, delimiter=',')
                    for row in reader:
                        name = row['name']
                        price = row['price']
                        quantity = row['quantity']
                        item = cls(name, price, quantity)

                    return cls.all
        return 'no value found'

    @staticmethod
    def string_to_number(num: str):
        """
        метод возвращающий число из числа-строки
        """
        return round(int(float(num)))

    def __add__(self, other):
        if not isinstance(other, Item):
            raise ValueError('Объект не принадлежит классам Phone и Item.')
        return self.quantity + other.quantity


class InstantiateCSVError(BaseException):
    a = 'InstantiateCSVError: Файл item.csv поврежден'
