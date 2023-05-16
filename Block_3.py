from random import choice
from typing import Callable


# Задача №1

"""
1.1 Написать декоратор, который перед запуском произвольной функции с произвольным набором аргументов будет
показывать в консоли сообщение "Покупайте наших котиков!" и возвращать результат запущенной функции.

1.2 Параметризовать декоратор таким образом, чтобы сообщение, печатаемое перед выполнением функции можно было
задавать как параметр во время декорирования.
"""



def my_func(any_func: Callable) -> Callable:
    print("Покупайте наших котиков!")
    def inner(*args, **kwargs):
        return any_func(*args, **kwargs)

    return inner


def summarized(num_1, num_2, *args, **kwargs):
    if kwargs:
        data = choice(list(kwargs.values()))
        result = num_1 + num_2 + sum(args[0:2]) + data
    else:
        result = num_1 + num_2 + sum(args[0:2])

    return result


