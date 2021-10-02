#!/usr/bin/env python

"""
Напишите *генератор* пар соседних чисел Фибоначчи (в функции вместо `result`
будет `yield`):

(1, 1), (1, 2), (2, 3), (3, 5), (5, 8) ...

https://en.wikipedia.org/wiki/Fibonacci_number

С помощью генератора найдите 2 таких числа Фибоначчи, через которые можно
будет вычислить золотое сечение c заданной точностью.

https://en.wikipedia.org/wiki/Golden_ratio#Relationship_to_Fibonacci_sequence
"""

# Golden Ratio
from collections import deque
from decimal import Decimal
from fractions import Fraction
from itertools import dropwhile
from typing import Generator, Tuple


def get_sqrt_5(precision: Decimal) -> Fraction:
    """
    Returns rational approximation of √5 constant
    with minimal denominator according to Hurwitz's
    theorem in field of number theory.
    """
    mantiss = Fraction(1, 4)
    curr_prescision = dec_one = Decimal(1)  # noqa: WPS429
    while curr_prescision > precision:
        mantiss = 1 / (4 + mantiss)
        curr_prescision = dec_one / Decimal(2 * mantiss.denominator ** 2)
    return 2 + mantiss


def fib_gen() -> Generator[int, None, None]:
    """
    Generator to produce Fibonacci numbers indefinitely.
    """
    yield from ((prev := 1), (curr := 1))  # noqa: WPS332
    while True:  # noqa: WPS457
        prev, curr = curr, prev + curr
        yield curr


def fib_pair_gen(unary_fib_iter) -> Generator[Tuple[int, int], None, None]:
    """
    Produce fibonacci numbers pairs

    It possible to get pairs direct from
    fibonacci one-by-one generator but i
    wanted trying to build more sophisticated
    «architecture» to be able parametrize fibonacci source
    """
    fib = unary_fib_iter
    tail = deque((next(fib),), maxlen=2)
    while True:  # noqa: WPS457
        tail.append(next(fib))
        yield (tail[0], tail[1])


def fib_phi_calc(precision: Decimal) -> Tuple[int, int]:
    """
    Returns 2 consecutive Fibonacci numbers to calculate
    Golden Ratio rational approximation with a given precision.
    """
    sqrt_5 = get_sqrt_5(precision)  # noqa: WPS114
    precision_cond = 1 / (sqrt_5 * Fraction(*precision.as_integer_ratio()))
    fpg = fib_pair_gen(fib_gen())
    phi_rat_iter = dropwhile(lambda pair: pair[0] ** 2 < precision_cond, fpg)
    return next(phi_rat_iter)
