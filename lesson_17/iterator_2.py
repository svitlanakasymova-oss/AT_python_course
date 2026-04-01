"""Напишіть ітератор, який повертає всі парні числа в діапазоні від 0 до N."""


class NumberIterator:
    def __init__(self, number):
        self.current_number = 0
        self.number = number

    def __iter__(self):
        return self

    def __next__(self):
        while self.current_number < self.number:
            if self.current_number % 2 == 0:
                tmp = self.current_number
                self.current_number += 1
                return tmp
            else:
                self.current_number += 1
                pass
        raise StopIteration()