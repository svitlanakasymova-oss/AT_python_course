"""Створіть клас Employee, який має атрибути name та salary.
Далі створіть два класи, Manager та Developer, які успадковуються від Employee.
Клас Manager повинен мати додатковий атрибут department, а клас Developer - атрибут programming_language.
Тепер створіть клас TeamLead, який успадковується як від Manager, так і від Developer.
Цей клас представляє керівника з команди розробників.
Клас TeamLead повинен мати всі атрибути як Manager (ім'я, зарплата, відділ), а також атрибут team_size,
який вказує на кількість розробників у команді, якою керує керівник.
Напишіть тест, який перевіряє наявність атрибутів з Manager та Developer у класі TeamLead
"""
class Employee:
    def __init__(self, name, salary, **kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.salary = salary

class Manager(Employee):
    def __init__(self, department, **kwargs):
        super().__init__(**kwargs)
        self.department = department

class Developer(Employee):
    def __init__(self, programming_language, **kwargs):
        super().__init__(**kwargs)
        self.programming_language = programming_language

class TeamLead(Manager, Developer):
    def __init__(self, team_size, **kwargs):
        super().__init__(**kwargs)
        self.team_size = team_size


def test_team_lead_attributes():
    test_lead = TeamLead(5,
                         salary=100,
                         department='QA',
                         programming_language='Python',
                         name='Svitlana')
    expected_params = ('name', 'salary', 'department', 'programming_language', 'team_size')
    for param in expected_params:
        assert getattr(test_lead, param), f"The following parameter is missing: {param}"
    print("✅ Test passed")

test_team_lead_attributes()