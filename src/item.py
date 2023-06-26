import csv

from src.InstantiateCSVError import InstantiateCSVError

class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        self.all.append(self)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"

    def __str__(self) -> str:
        return self.name

    def __add__(self, other_instance) -> int:
        if not issubclass(other_instance.__class__, self.__class__):
            raise TypeError('Возможно сложить только с экземплярами Phone или Item классов')
        return self.quantity + other_instance.quantity

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str) -> None:
        self.__name = name if len(name) <= 10 else 'Exception: Длина наименования товара превышает 10 символов.'

    @classmethod
    def instantiate_from_csv(cls, path=r"../src/items.csv"):
        """
        Инициализирует экземпляры класса `Item` данными из файла _src/items.csv
        """

        try:
            with open(path, newline='') as file:
                reader = csv.DictReader(file)
                cls.all.clear()
                try:
                    for row in reader:
                        item = (cls(row['name'], row['price'], row['quantity']))
                except KeyError:
                    raise InstantiateCSVError('Файл items.csv поврежден')
        except FileNotFoundError:
            raise FileNotFoundError('Отсутствует файл items.csv')

    @staticmethod
    def string_to_number(number: str) -> int:
        return int(float(number))
