from random import choice


# Easy
# counter = 0
# def summarized(num_1, num_2, num_3, num_4, *args, **kwargs):
#     if kwargs:
#         data = choice(list(kwargs.values()))
#         result = num_1 + num_2 + num_3 + num_4 + sum(args[0:2]) + data
#     else:
#         result = num_1 + num_2 + num_3 + num_4 + sum(args[0:2])
#     global counter
#     counter += 1
#     return result


# print(f"Сумма равна: {summarized(1, 1, 1, 1, 2, 2, num_5=3, num_6=10)}, счетчик равен: {counter}")
# print(f"Сумма равна: {summarized(1, 1, 2, 2, 3, 3, num_5=20, num_6=30)}, счетчик равен: {counter}")


# Medium

# counter = 0
# def summarized(num_1, num_2, num_3, num_4, *args, **kwargs):
#     if kwargs:
#         data = choice(list(kwargs.values()))
#         result = num_1 + num_2 + num_3 + num_4 + sum(args[0:2]) + data
#     else:
#         result = num_1 + num_2 + num_3 + num_4 + sum(args[0:2])
#     global counter
#     counter += 1
#     return result

# def summarized_2(num_1, num_2):
#     result = num_1 + num_2
#     global counter
#     counter += 1
#     return result
#
#
# def summarized_3(*args, **kwargs):
#     result = sum(args) + sum(kwargs.values())
#     global counter
#     counter += 1
#     return result
#
#
# def summarized_4(num_1, *args):
#     result = num_1 + sum(args)
#     global counter
#     counter += 1
#     return result
#
#
# print(f"Сумма чисел равна: "
#       f"{summarized(1, 1, 1, 1, 10) + summarized_2(2, 2) + summarized_3(num_1=10, num_2=10) + summarized_4(2, 4)}\n"
#       f"Счетчик равен: {counter}")


# counter = 0
# def func():
#     print("Вызов функции func")
#     def summarized(num_1, num_2, num_3, num_4, *args, **kwargs):
#         if kwargs:
#             data = choice(list(kwargs.values()))
#             result = num_1 + num_2 + num_3 + num_4 + sum(args[0:2]) + data
#         else:
#             result = num_1 + num_2 + num_3 + num_4 + sum(args[0:2])
#         global counter
#         counter += 1
#         return result
#     return summarized

# var = func()
# print(var)
# """После печати переменной var результатом работы функции func является возврат адреса в памяти локальной функции
# суммирования"""
# print(var(1, 2, 3, 4))
# """После вызова функции суммирования через переменную я получаю результат ее работы, если передаю аргументы. Без
# передачи аргументов получаю ошибку."""


# Hard

# def func():
#     print("Вызов функции func")
#     counter = 0
#     def summarized(num_1, num_2, num_3, num_4, *args, **kwargs):
#         if kwargs:
#             data = choice(list(kwargs.values()))
#             result = num_1 + num_2 + num_3 + num_4 + sum(args[0:2]) + data
#         else:
#             result = num_1 + num_2 + num_3 + num_4 + sum(args[0:2])
#         nonlocal counter
#         counter += 1
#         print(counter)
#         return result
#     return summarized
#
# var = func()
# print(var(1, 2, 3, 4))
# print(var(1, 2, 3, 4))
# print(var(1, 2, 3, 4))
# print(var(1, 2, 3, 4))