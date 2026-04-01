"""Реалізуйте ітератор для зворотного виведення елементів списку."""


class ListReverveIterator:
    def __init__(self, lst):
        self.lst = lst
        self.index = len(self.lst)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index > 0:
            self.index -= 1
            return self.lst[self.index]
        else:
            raise StopIteration