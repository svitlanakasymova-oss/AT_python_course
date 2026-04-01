"""Напишіть генератор, який повертає послідовність парних чисел від 0 до N."""


def generate_even_numbers(start, end):
    for number in range(start, end):
        if number % 2 == 0:
            yield number