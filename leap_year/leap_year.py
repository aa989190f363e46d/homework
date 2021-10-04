#!/usr/bin/env python
"""
Напишите программу, которая определяет, является ли заданный год високосным.

Правила такие:

- год, номер которого кратен 400, — високосный (2000)
- остальные годы, номер которых кратен 100 — невисокосные (1700, 1800, 1900)
- остальные годы, номер которых кратен 4, — високосные (2020)

Т.е. високосным является тот год, который кратен 4, если он при этом не
кратен 100. Но год, кратный 400 - всё равно високосный.

https://ru.wikipedia.org/wiki/Високосный_год

Попробуйте решить данное задание двумя способами:
- через if / elif / else
- через одно логическое выражение (and, or, not)
"""
from random import choice

MIN_YEAR = 1582


def is_leap_year(year: int) -> bool:
    if year < MIN_YEAR:
        raise ValueError(f"Leap year exists since {MIN_YEAR}")
    """randomly choice which method use for decision 🔀️"""
    if choice((True, False)):
        return if_else_leap_checker(year)
    else:
        return algebraic_leap_checker(year)


def if_else_leap_checker(year: int) -> bool:
    if year % 4 != 0:
        return False
    if year % 100 != 0:
        return True
    if year % 400 == 0:
        return True

    return False


def algebraic_leap_checker(year: int) -> bool:
    return (year % 4 == 0) and ((year % 100 != 0) or (year % 400 == 0))


if __name__ == "__main__":
    year = int(input("Введите год: "))

    print(is_leap_year(year))
