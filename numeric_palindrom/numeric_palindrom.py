#!/usr/bin/env python

"""
Напишите функцию, которая проверяет, является ли целое положительное число
палиндромом.

Можно работать только с числами, конвертировать в строку нельзя :)
"""
from math import log10
from typing import List


def is_palindrom(num: int) -> bool:
    if num <= 0:
        raise ValueError('Number must be a positive')
    if int(num) != num:
        raise ValueError('Number must be a integer')

    digits = split_into_digits(num)
    mid_point = sum(divmod(len(digits), 2))
    cross = zip(digits[:mid_point], reversed(digits))
    return all((beg == end for beg, end in cross))


def split_into_digits(num: int) -> List[int]:
    num_len = int(log10(num)) + 1
    powers = [10 ** pw for pw in range(num_len + 1)]
    bounds = zip(powers[1:], powers)
    return [extract_digit(num, low, up) for low, up in bounds]


def extract_digit(num, low, up):
    return (num % up - num % low) / up
