# Easy
def my_func(my_string = "test", any_num = 3) -> str:
    string_to_add = my_string
    if any_num == 1:
        return my_string
    else:
        for num in range(1, any_num + 1):
            if num == 1:
                continue
            if num % 2 == 0:
                my_string += string_to_add.upper()
            else:
                my_string += string_to_add.lower()
        return my_string

variable = my_func()
print(variable) # результат - вывод в терминал 'testTESTtest'
print(sum(variable))
'''вызвал функцию суммирования через переменную? выдало ошибку unsupported operand type(s) for +: 'int' and 'str.
в функцию sum() передается же итерируемый объект, а мы передаем строку'''

#Medium
def summarized(num_1, num_2, num_3, num_4, *args):
    result = num_1 + num_2 + num_3 + num_4 + sum(args)
    return result

print(summarized(10)) #№1 - выдет ошибку, поскольку не переданы еще 3 обязательных аргумента

print(summarized(10, num_1=10)) #№2 -ошибка, поскольку позиционно и по ключу передаем в один обязательный аргумент num_1

my_tuple = 1, 2, 3, 4, 5
print(summarized(*my_tuple)) # №3 - кортеж распаковал первые 4 числа в позиционные аргументы, а последнее число добавил
# в args, после просуммировал их и вывел результат

my_dict = {"num_1": 1, "num_2": 2, "num_3": 3, "num_4": 4, "num_5": 5}
print(summarized(*my_dict)) # №4 ошибка, поскольку переданы в функцию ключи словаря
print(summarized(**my_dict)) # распаковываем весь словарь и выдает ошибку потому что не num_5 нет в функции

# Hard

from random import choice
def summarized(num_1, num_2, num_3, num_4, *args, **kwargs):
    if kwargs:
        data = choice(list(kwargs.values()))
        result = num_1 + num_2 + num_3 + num_4 + sum(args[0:2]) + data
    else:
        result = num_1 + num_2 + num_3 + num_4 + sum(args[0:2])
    return result

print(summarized(1, 2, 3, 4, 5, 6, 7, 8, num_5=1, num_6=2, num_7=3))