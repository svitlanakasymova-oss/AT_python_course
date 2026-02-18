"""Створіть масив зі строками, які будуть складатися з чисел, які розділені комою.
Наприклад: [”1,2,3,4”, ”1,2,3,4,50” ”qwerty1,2,3”]
Для кожного елементу списку виведіть суму всіх чисел (створіть нову функцію для цього).
Якщо є символи, що не є числами (”qwerty1,2,3” у прикладі), вам потрібно зловити виняток і вивести “Не можу це зробити!”
Використовуйте блок try/except, щоб уникнути інших символів, окрім чисел у списку.
Для цього прикладу правильний вивід буде - 10, 60, “Не можу це зробити”"""


def split_array(array):
    split_list = []
    for item in array:
        temp = item.split(',')
        split_list.append(temp)
    return split_list

def calculate_sum(array): #[['1', '2', '3', '4'], ['1', '2', '3', '4', '50'], ['qwerty1', '2', '3']]
    sum_list = []
    for item in array: #тут в нас item = ['1', '2', '3', '4']
        res = 0
        for rec in item:
            try:
                res += int(rec)
            except ValueError:
                res = "Не можу це зробити"
                break
        sum_list.append(res)
    return sum_list


arr = split_array(['1,2,3,4', '1,2,3,4,50', 'qwerty1,2,3'])
print(calculate_sum(arr))