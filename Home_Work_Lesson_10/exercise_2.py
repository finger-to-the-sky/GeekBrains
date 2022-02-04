# Решение задачи №2

# Импортируем модуль abc и абстрактный метод
from abc import ABC, abstractmethod


class Clothes(ABC):

    # Конструктор для хранения данных
    def __init__(self, param):
        self.param = param

    # Обозначаем абстрактный метод и создаем метод для рассчета
    @abstractmethod
    #
    def expense(self):
        pass

    # Конструктор строки с помощью которого будем возвращать значения в строке
    def __str__(self):
        return str(self.param)


# Создаем класс для Пальто
class Coat(Clothes):

    # Декорируем метод рассчета и производим его по заданным значениям
    @property
    def expense(self):
        return self.param / 6.5 + 0.5


# Далее создаем класс Костюм
class Suit(Clothes):

    # Декорируем метод и так же производим рассчет для костюма
    @property
    def expense(self):
        return self.param * 2 + 0.3


# Создаем экземпляры и проверяем работу методов

a = Coat(13)
b = Suit(2.2)
print(a)
print(a.expense)
print(b.expense)
