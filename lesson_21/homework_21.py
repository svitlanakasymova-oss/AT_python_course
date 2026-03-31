import dbm.sqlite3
from datetime import date
from lesson_21.data_arrays import first_names, last_names
from lesson_21.model import create_student, create_course, get_student_list, enroll_student_to_specific_course, \
    get_courses_list, get_course_by_id, get_students_list_by_certain_course, get_courses_by_student, \
    get_student_by_name, change_email, get_courses_by_start_date, change_course_start_date, delete_student
import random


#додаємо 10 студентів в базу даних
for i in range (0, 10):
    create_student(first_name = random.choice(first_names),
                   last_name= random.choice(last_names),
                   date_of_birth = date(random.randint(1980, 2005), random.randint(1, 12), random.randint(1, 28)),
                   email = f'test_email{random.randint(1, 10000)}{random.randint(1, 10000)}@gmail.com',)

#додаємо 5 курсів
for i in range (0, 5):
    create_course(
        title= f'Курс з прогулювання занять. Частина {random.randint(1, 5)}',
        start_date= date(random.randint(2026, 2027), random.randint(1, 12), random.randint(1, 28))
    )

#кожного студента енролимо на якийсь із курсів
for student in get_student_list():
    enroll_student_to_specific_course(student, random.choice(get_courses_list()))

#виведемо список всіх студентів, записаних на перший курс
for student in get_students_list_by_certain_course(get_course_by_id(1)):
    print(f'{student.first_name} {student.last_name}, {student.date_of_birth}, {student.email}')

#виведемо список всіх курсів, на які зареєстрований студент
for course in get_courses_by_student(get_student_by_name("Mia", "Morgan")):
    print(f'Course: {course.title}. Start date: {course.start_date}')


#змінюємо студентці емейл
studentessa = get_student_by_name('Mia', 'Morgan')
change_email(studentessa, 'this_is_new_email@gmail.com')


#відкладемо всі курси на наступний рік
for course in get_courses_by_start_date('2027-01-01'):
    change_course_start_date(course, '2027-01-01')


#видаляємо студента
print(f'{get_student_by_name('Caroline', 'Wilson').first_name} {get_student_by_name('Caroline', 'Wilson').last_name},'
      f' {get_student_by_name('Caroline', 'Wilson').email}')
delete_student(get_student_by_name('Caroline', 'Wilson').id)
try:
    print(get_student_by_name('Caroline', 'Wilson').first_name)
except AttributeError as e:
    print("Успішно видалений")