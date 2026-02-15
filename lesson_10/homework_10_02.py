"""Завдання 2
Створіть абстрактний клас "Фігура" з абстрактними методами для отримання площі та периметру.
Наслідуйте від нього декілька (> 2) інших фігур, та реалізуйте математично вірні для них методи для площі та периметру.
Властивості по типу “довжина сторони” й т.д. повинні бути приватними, та ініціалізуватись через конструктор.
Створіть Декілька різних об’єктів фігур, та у циклі порахуйте та виведіть в консоль площу та периметр кожної."""
from abc import ABC, abstractmethod
import math


class Figure(ABC):
    @abstractmethod
    def calculate_area(self):
        ...

    @abstractmethod
    def calculate_perimeter(self):
        ...

class Square(Figure):
    def __init__(self, side):
        self.__side = side

    def calculate_area(self):
        return self.__side * self.__side

    def calculate_perimeter(self):
        return self.__side * 4


#реалізовано тільки для формули Герона
class Triangle(Figure):
    def __init__(self, side_a, side_b, side_c):
        self.__side_a = side_a
        self.__side_b = side_b
        self.__side_c = side_c

    def calculate_area(self):
        p2 = (self.__side_a + self.__side_b + self.__side_c) / 2
        area = math.sqrt(p2 * (p2 - self.__side_a) * (p2 - self.__side_b) * (p2 - self.__side_c))
        return area

    def calculate_perimeter(self):
        return (self.__side_a + self.__side_b + self.__side_c)


class Circle(Figure):
    def __init__(self, radius):
        self.__radius = radius

    def calculate_area(self):
        return math.pi * (self.__radius * self.__radius)

    def calculate_perimeter(self):
        return 2 * math.pi * self.__radius


square = Square(1.8)
triangle = Triangle(4, 1, 4)
circle = Circle(3.5)

for figure in [square, triangle, circle]:
    print(f'Фігура - {figure.__class__.__name__}')
    print(f'Площа = {float(figure.calculate_area()).__round__(2)}')
    print(f'Периметр = {float(figure.calculate_perimeter()).__round__(2)}')