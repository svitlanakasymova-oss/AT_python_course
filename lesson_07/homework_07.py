# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та виправити\доповнити.
"""
import math


def multiplication_table(number):
    multiplier = 1
    while True:
        result = number * multiplier
        if  result > 25:
            break
        else:
            print(str(number) + "x" + str(multiplier) + "=" + str(result))
            multiplier += 1

multiplication_table(3)


# task 2
"""Написати функцію, яка обчислює суму двох чисел."""
def calculate_sum(n1, n2):
    return n1 + n2
print(calculate_sum(3, 4))


# task 3
"""Написати функцію, яка розрахує середнє арифметичне списку чисел."""
def calculate_average(lst: list):
    return sum(lst)/len(lst)
print(calculate_average([1, 2, 3, 4, 5, 17, -3, 0]))


# task 4
"""Написати функцію, яка приймає рядок та повертає його у зворотному порядку."""
def reverse_string(st: str):
    return "".join(reversed(st))
print(reverse_string("hello"))


# task 5
"""Написати функцію, яка приймає список слів та повертає найдовше слово у списку."""
def find_longest(lst: list):
    length = 0
    word = ""
    for item in lst:
        if len(item) > length:
            word = item
            length = len(item)
    return word
print(find_longest(["Hello", "my", "name", "is", "Svitlana"]))


# task 6
"""Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""
def find_substring(str1, str2):
    temp_str = str1
    for i in range(len(str1)):
        if temp_str.startswith(str2):
            return i
        else:
            temp_str = temp_str[1:]
    return -1

str1 = "Hello, world!"
str2 = "world"
print(find_substring(str1, str2)) # поверне 7

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(find_substring(str1, str2)) # поверне -1


"""Оберіть будь-які 4 таски з попередніх домашніх робіт та перетворіть їх у 4 функції,
що отримують значення та повертають результат.
Обовʼязково документуйте функції та дайте зрозумілі імена змінним."""


# task 7
""" (6.3) Напишіть код, який сформує новий list (наприклад lst2), який містить лише змінні типу стрінг, які присутні в lst1.
Дані в лісті можуть бути будь-якими."""
def clean_non_string_items(lst: list):
    clean_list = []
    for item in lst:
        if isinstance(item, str):
            clean_list.append(item)
    return clean_list
print(clean_non_string_items(['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']))


# task 8
""" (4.4) Виведіть, скільки разів у тексті зустрічається літера "h" (змінено на задану в функцію літеру)"""
def calculate_frequency(st: str, letter: str):
    if len(letter) == 1:
        frequency = 0
        for ch in st:
            if ch == letter:
                frequency += 1
        return frequency
    else:
        return None
print(calculate_frequency("Here is my test string. Please use it for appropriate reason", "s"))


# task 9
""" (3.8)
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
def calculate_total_price(amount: int, price: int):
    return amount * price

big_pizza = calculate_total_price(4, 274)
medium_pizza = calculate_total_price(4, 218)
juice = calculate_total_price(4, 35)
cake = calculate_total_price(1, 350)
water = calculate_total_price(3, 21)
total_price = big_pizza + medium_pizza + juice + cake + water


# task 10
""" (3.9)
Ігор займається фотографією. Він вирішив зібрати всі свої 232
фотографії та вклеїти в альбом. На одній сторінці може бути
розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
Ігорю, щоб вклеїти всі фото?
"""
def calculate_page_amount(photo_amount: int):
    return math.ceil(photo_amount/8)
print(calculate_page_amount(232))
