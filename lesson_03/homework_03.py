# task 01 == Розділіть змінну alice_in_wonderland так, щоб вона займала декілька фізичних ліній
import math
from math import remainder

alice_in_wonderland = ''' "Would you tell me, please, which way I ought to go from here?"
"That depends a good deal on where you want to get to," said the Cat.
"I don't much care where ——" said Alice.
"Then it doesn't matter which way you go," said the Cat.
"—— so long as I get somewhere," Alice added as an explanation.
"Oh, you're sure to do that," said the Cat, "if you only walk long enough." '''

# task 02 == Знайдіть та відобразіть всі символи одинарної лапки (') у тексті
for char in alice_in_wonderland:
    if char == "'":
        print(char)

# task 03 == Виведіть змінну alice_in_wonderland на друк

print(alice_in_wonderland)

"""
    # Задачі 04 -10:
    # Переведіть задачі з книги "Математика, 5 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в п'ятому класі
"""


# task 04
"""
Площа Чорного моря становить 436 402 км2, а площа Азовського
моря становить 37 800 км2. Яку площу займають Чорне та Азов-
ське моря разом?
"""
black_sea = 436_402
azov_sea = 37_800
total_area = black_sea + azov_sea
print(f"Разом Чорне та Азовське море займають {total_area} км2")


# task 05
"""
Мережа супермаркетів має 3 склади, де всього розміщено
375 291 товарів. На першому та другому складах перебуває
250 449 товарів. На другому та третьому – 222 950 товарів.
Знайдіть кількість товарів, що розміщені на кожному складі.
"""
total_amount = 375_291
first_second_total = 250_449
second_third_total = 222_950
first = total_amount - second_third_total
second = first_second_total - first
third = total_amount - first_second_total
print(f"На першому складі розміщено {first} товарів. \nНа другому складі розміщено {second} товарів. \nНа третьому складі розміщено {third} товарів.")


# task 06
"""
Михайло разом з батьками вирішили купити комп’ютер, скориставшись послугою «Оплата частинами».
Відомо, що сплачувати необхідно буде півтора року по 1179 грн/місяць.
Обчисліть вартість комп’ютера.
"""
payment = 1179
duration = 18
cost = payment * duration
print(f"Загальна вартість компʼютера становить {cost} гривень.")


# task 07
"""
Знайди остачу від ділення чисел:
a) 8019 : 8     d) 7248 : 6
b) 9907 : 9     e) 7128 : 5
c) 2789 : 5     f) 19224 : 9
"""
a = 8019 % 8
b = 9907 % 9
c = 2789 % 5
d = 7248 % 6
e = 7128 % 5
f = 19224 % 9


# task 08
"""
Іринка, готуючись до свого дня народження, склала список того,
що їй потрібно замовити. Обчисліть, скільки грошей знадобиться
для даного її замовлення.
Назва товару    Кількість   Ціна
Піца велика     4           274 грн
Піца середня    2           218 грн
Сік             4           35 грн
Торт            1           350 грн
Вода            3           21 грн
"""
cost_pizza_grand = 4 * 274
cost_pizza_medium = 2 * 218
cost_juice = 4 * 35
cost_cake = 1 * 350
cost_water = 3 * 21
total_cost = cost_pizza_grand + cost_pizza_medium + cost_juice + cost_cake + cost_water
print(f"Для даного замовлення Іринці знадобиться {total_cost} грн.")


# task 09
"""
Ігор займається фотографією. Він вирішив зібрати всі свої 232
фотографії та вклеїти в альбом. На одній сторінці може бути
розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
Ігорю, щоб вклеїти всі фото?
"""
photo_amount = 232
page_max = 8
pages_amount = math.ceil(photo_amount / page_max)
print(f"Ігорю знадобиться {pages_amount} сторінок.")


# task 10
"""
Родина зібралася в автомобільну подорож із Харкова в Будапешт.
Відстань між цими містами становить 1600 км.
Відомо, що на кожні 100 км необхідно 9 літрів бензину.
Місткість баку становить 48 літрів.
1) Скільки літрів бензину знадобиться для такої подорожі?
2) Скільки щонайменше разів родині необхідно заїхати на заправку під час цієї подорожі, кожного разу заправляючи повний бак?
"""
distance = 1600
fuel_consumption_basic = 9
fuel_needed = (distance/100) * fuel_consumption_basic
print(f"Для подорожі з Харкова в Будапешт знадобиться {fuel_needed} літрів бензину.")
tank_capacity = 48
refueling_stops = math.ceil(fuel_needed / tank_capacity)
print(f"Родині необхідно заїхати на заправку щонайменше {refueling_stops} разів(и), за умови, що при старті подорожі бак вважати пустим.")