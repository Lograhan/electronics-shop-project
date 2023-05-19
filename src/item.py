import csv

with open("/home/roman/skypro/electronics-shop-project/src/items.csv", encoding="1251") as file:
    data = csv.DictReader(file)

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
        Item.all.append(self.__name)



    @property
    def set_name(self):
        x = self.__name
        if len(x) > 10:
            raise Exception("Длина наименования товара больше 10 символов")
        else:
            return x

    def get_name(self):
        return self.__name

    @staticmethod
    def string_to_number(x):
        x = int(x)
        return x

    def __repr__(self):
        return f'{self.calculate_total_price()}'

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        total = self.price * self.quantity
        return total

    def apply_discount(self) -> float:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = self.price * Item.pay_rate
        return self.price

    def instantiate_from_csv():
        new_data = data
        for i in new_data:
            x = Item(i['name'], i['price'], i['quantity'])
            return x



