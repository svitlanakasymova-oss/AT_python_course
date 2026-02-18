"""На вхід функції потрапляють строки лог-файлу виду:

2023-04-27 15:30:45 - TestCase: login_successful
2023-04-27 15:35:12 - TestCase: invalid_password

Після строки 'TestCase: ' йде назва тесту.
Зробити так, щоб функція виводила лише назву тесту.

Увага! Замість print у функії використовуйте return."""


def solution(test_string):
    if "TestCase: " in test_string:
        return test_string[32:]
    else:
        return test_string