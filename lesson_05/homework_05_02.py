# Given list of tuples (name, surname, age, profession, City location)
# 1 - Add your new record o the beginning of the given list
# 2 - In modified list swap elements with indexes 1 and 5 (1<->5). Print result
# 3 - check that all people in modified list with records indexes 6, 10, 13 have age >=30. Print condition check result

people_records = [
  ('John', 'Doe', 28, 'Engineer', 'New York'),
  ('Alice', 'Smith', 35, 'Teacher', 'Los Angeles'),
  ('Bob', 'Johnson', 45, 'Doctor', 'Chicago'),
  ('Emily', 'Williams', 30, 'Artist', 'San Francisco'),
  ('Michael', 'Brown', 22, 'Student', 'Seattle'),
  ('Sophia', 'Davis', 40, 'Lawyer', 'Boston'),
  ('David', 'Miller', 33, 'Software Developer', 'Austin'),
  ('Olivia', 'Wilson', 27, 'Marketing Specialist', 'Denver'),
  ('Daniel', 'Taylor', 38, 'Architect', 'Portland'),
  ('Grace', 'Moore', 25, 'Graphic Designer', 'Miami'),
  ('Samuel', 'Jones', 50, 'Business Consultant', 'Atlanta'),
  ('Emma', 'Hall', 31, 'Chef', 'Dallas'),
  ('William', 'Clark', 29, 'Financial Analyst', 'Houston'),
  ('Ava', 'White', 42, 'Journalist', 'San Diego'),
  ('Ethan', 'Anderson', 36, 'Product Manager', 'Phoenix')
]

# 1 - Add your new record o the beginning of the given list
people_records.insert(0, ('Svitlana', 'Kasymova', 31, 'QA Engineer', 'Irpin'))


# 2 - In modified list swap elements with indexes 1 and 5 (1<->5). Print result
temp_storage = people_records.pop(1)
people_records.insert(1, people_records.pop(4))
people_records.insert(5, temp_storage)
print(people_records)

# 3 - check that all people in modified list with records indexes 6, 10, 13 have age >=30. Print condition check result
total_check = True
for i in range(6, 10, 13):
    if people_records[i][2] < 30:
        total_check = False
        break
print("Всі люди в заданому пошуку мають принаймні 30 років" if total_check else "Перевірку на вік не пройдено. Декому немає 30 років")
