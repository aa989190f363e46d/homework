#!/usr/bin/env python

"""
Напишите функцию, которая выводят n-ое число Фибоначчи.
Разрешается использовать временные переменные, циклы и условные операторы.

https://en.wikipedia.org/wiki/Fibonacci_number
https://en.wikipedia.org/wiki/Generalizations_of_Fibonacci_numbers
"""
from itertools import islice


def fibonacci(num: int) -> int:
    if int(num) != num:
        raise ValueError('Index must be integer')
    if num == 0:
        """
        Case was extracted in according
        to generalizing generator for
        negative numbers
        """
        return 0
    mod_n = abs(num)
    fib_gen = islice(fibonacci_gen(), mod_n - 1, mod_n)
    sign_mul = 1
    if num < 0:
        sign_mul = (-1) ** ((mod_n - 1) % 2)
    return sign_mul * next(fib_gen)


def fibonacci_gen():
    prev, curr = 1, 1
    yield from (prev, curr)
    while True:  # noqa: WPS457
        prev, curr = curr, prev + curr
        yield curr
