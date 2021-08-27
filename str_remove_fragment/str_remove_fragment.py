#!/usr/bin/env python

"""
Задача об удалении выделенной подстроки.

Напишите функцию, которая принимает на вход строку `s` и некоторый сепаратор
`sep`. Функция должна удалить из строки всё, что находится между первым и
последним сепаратором, а также их самих. Если таких сеператоров в строке
меньше двух, вернуть исходную строку.
"""


def remove_fragment(string: str, sep: str) -> str:
    try:
        left_bound = string.index(sep)
    except ValueError:
        return string
    len_sep = len(sep)
    try:
        right_bound = string.rindex(sep, left_bound + len_sep)
    except ValueError:
        return string
    return string[:left_bound] + string[right_bound + len_sep:]
