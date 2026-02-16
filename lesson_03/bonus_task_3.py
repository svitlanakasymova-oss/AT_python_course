"""Дано тризначне ціле число від 100 до 999.
Використовуючи лише арифметичні дії "перевернути" число.
Наприклад: 123 -> 321, 900 -> 9
Питання задачі
Написати код, який за допомогою лише арифметичних дій змінить порядок цифр в цілому числі на зворотній"""


def solution(x):
    number = x
    reversed_number = 0
    while number > 0:
        reversed_number = reversed_number * 10 + number % 10
        number = number // 10
    return reversed_number