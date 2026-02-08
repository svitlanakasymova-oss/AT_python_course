"""Порахувати кількість унікальних символів в строці.
Якщо їх більше 10 - вивести в консоль True, інакше - False.
Строку отримати за допомогою функції input()"""

str = input()
symbols_set = set()
for ch in str:
    symbols_set.add(ch)
print(True if len(symbols_set) >= 10 else False)