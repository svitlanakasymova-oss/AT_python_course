"""Створіть клас геометричної фігури "Ромб".
Клас повинен мати наступні атрибути:
- сторона_а (довжина сторони a).
- кут_а (кут між сторонами a і b).
- кут_б (суміжний з кутом кут_а).

Для встановлення значень атрибутів використовуйте метод __setattr__.

Необхідно реалізувати наступні вимоги:
- Значення сторони сторона_а повинно бути більше 0.
- Кути кут_а та кут_б повинні задовольняти умову: кут_а + кут_б = 180
- Протилежні кути ромба завжди рівні, тому при заданому значенні кут_а, значення кут_б обчислюється автоматично."""


class Rhombus:
    #side_a - float
    #angle_a - float
    #angle_b - float
    def __setattr__(self, name, value):
        if name == 'side_a':
            if not isinstance(value, (int, float)) or isinstance(value, bool) or (value < 0):
                print(f"{value} = Невалідне значення сторони")
                return
        elif name in ('angle_a', 'angle_b') and (not isinstance(value, (int, float)) or isinstance(value, bool)):
            print(f"{value} = Невалідне значення кута")
            return
        super().__setattr__(name, value)
        if name in ('angle_a', 'angle_b') and isinstance(value, (int, float)):
            angle_a = getattr(self, 'angle_a', None)
            angle_b = getattr(self, 'angle_b', None)
            if angle_a is None and angle_b is None:
                print("Кути поки не задані")
            elif (angle_a is not None and angle_a >= 180) or (angle_b is not None and angle_b >= 180):
                print(f"{value} = Значення кута невалідне і має бути менше 180")
                self.__delattr__('angle_a') if getattr(self, 'angle_a', None) is not None else None
                self.__delattr__('angle_b') if getattr(self, 'angle_b', None) is not None else None
            elif (angle_a is not None and angle_a <= 0) or (angle_b is not None and angle_b <= 0):
                print(f"{value} = Значення кута невалідне і має бути більше 0")
                self.__delattr__('angle_a') if getattr(self, 'angle_a', None) is not None else None
                self.__delattr__('angle_b') if getattr(self, 'angle_b', None) is not None else None
            elif isinstance(angle_a, (int, float)):
                object.__setattr__(self, 'angle_b', 180 - self.angle_a)
            elif isinstance(angle_b, (int, float)):
                object.__setattr__(self, 'angle_a', 180 - self.angle_b)