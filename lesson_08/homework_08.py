"""Створіть клас "Студент" з атрибутами "ім'я", "прізвище", "вік" та "середній бал".
Створіть об'єкт цього класу, представляючи студента.
Потім додайте метод до класу "Студент", який дозволяє змінювати середній бал студента.
Виведіть інформацію про студента та змініть його середній бал."""

class Student:
    """Клас студент матиме атрибути "ім'я", "прізвище", "вік" та "середній бал\""""
    def __init__(self, first_name, last_name, age, average_score):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.average_score = average_score

    def change_score(self, new_score):
        self.average_score = new_score

    def print_description(self):
        print(f"Student name is {self.first_name} {self.last_name}. Is {self.age} years old. Average score is {self.average_score}.")

svitlana = Student("Svitlana", "Kasymova", 31, "99")
svitlana.print_description() #before change
svitlana.change_score(100)
svitlana.print_description() #after change