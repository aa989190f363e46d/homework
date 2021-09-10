#!/usr/bin/env python

"""
Напишите функцию, которая возвращает для чисел:

- кратных 3 - Fizz
- кратных 5 - Buzz
- одновременно кратных и 3 и 5 - FizzBuzz
- строковое представление этих чисел (т.е. "1" для 1)

https://en.wikipedia.org/wiki/Fizz_buzz
"""


def fizzbuzz(num: int) -> str:
    if num <= 0:
        raise ValueError(f'Wron value ({num})')
    fizz = 'Fizz' if num % 3 == 0 else ''
    buzz = 'Buzz' if num % 5 == 0 else ''
    reply = f'{fizz}{buzz}'
    if not reply:
        return f'{num}'
    return reply
