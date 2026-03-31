from sqlalchemy import Column, Table, ForeignKey, CheckConstraint
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy.sql.sqltypes import Integer, String, Date

from lesson_21.database import get_db, db_gen, db

Base = declarative_base()

student_course_relation = Table('student_course_relation',
                                Base.metadata,
                                Column('student_id', Integer, ForeignKey('students.id', ondelete='CASCADE')),
                                Column('course_id', Integer, ForeignKey('courses.id', ondelete='CASCADE')),)

class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    first_name = Column(String(20), nullable=False)
    last_name = Column(String(20), nullable=False)
    date_of_birth = Column(Date, nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    courses = relationship('Course', secondary=student_course_relation, back_populates='students')

class Teacher(Base):
    __tablename__ = 'teachers'
    id = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    specialization = Column(String)
    courses = relationship('Course', back_populates='teacher')

class Course(Base):
    __tablename__ = 'courses'
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    start_date = Column(Date, nullable=False)
    end_date = Column(Date)
    teacher_id = Column(Integer, ForeignKey('teachers.id', ondelete='SET NULL'), nullable=True)
    students = relationship('Student', secondary=student_course_relation, back_populates='courses')
    teacher = relationship('Teacher', back_populates='courses')

    __table_args__ = (
        CheckConstraint('end_date IS NULL OR end_date >= start_date', name='check_end_date_greater_start_date'),
    )


#додає студента в БД
def create_student(first_name, last_name, date_of_birth, email):
    student = Student(
        first_name = first_name,
        last_name = last_name,
        date_of_birth = date_of_birth,
        email = email)
    db.add(student)
    db.commit()


#додає новий курс
def create_course(title, start_date, end_date = None, teacher_id = None):
    course = Course(
        title = title,
        start_date = start_date,
        end_date = end_date,
        teacher_id = teacher_id
    )
    db.add(course)
    db.commit()


#витягаємо список всіх студентів
def get_student_list():
    return db.query(Student).all()


#витягаємо список всіх курсів
def get_courses_list():
    return db.query(Course).all()


#додає студента до певного курсу
def enroll_student_to_specific_course(student, course):
    student.courses.append(course)
    db.commit()


#отримує список всіх студентів, записаних на певний курс
def get_students_list_by_certain_course(course):
    return db.query(Student).filter(Student.courses.any(id=course.id)).all()


#отримує курс по айдішці
def get_course_by_id(course_id):
    return db.query(Course).get(course_id)


#витягаємо студента по імені + прізвищу
def get_student_by_name(first_name, last_name):
    return db.query(Student).filter(Student.first_name == first_name, Student.last_name == last_name).first()


#отримує список курсів для студента
def get_courses_by_student(student):
    return db.query(Course).filter(Course.students.any(id=student.id)).all()


#змінює студенту емейл
def change_email(student, new_email):
    student.email = new_email
    db.commit()


#змінює дату старту курсу
def change_course_start_date(course, new_start_date):
    course.start_date = new_start_date
    db.commit()


#знайти всі курси, старт яких раніше за вказану дату
def get_courses_by_start_date(start_date):
    return db.query(Course).filter(Course.start_date < start_date).all()


#видалити студента
def delete_student(student_id):
    db.query(Student).filter(Student.id == student_id).delete()
    db.commit()