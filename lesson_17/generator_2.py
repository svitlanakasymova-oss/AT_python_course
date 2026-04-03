"""Створіть генератор, який генерує послідовність Фібоначчі до певного числа N."""


def generate_fibonacci_numbers(end):
    n1 = 0
    n2 = 1
    temp = n1
    while n1 <= end:
        yield n1
        temp = n1
        n1 = n2
        n2 = temp + n2