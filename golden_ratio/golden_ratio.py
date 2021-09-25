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
from typing import Generator, Tuple

GOLDEN = (1 + 5 ** 0.5) / 2


def fib_gen() -> Generator[int, None, None]:
    """
    Generator to produce Fibonacci numbers indefinitely.
    """
    yield from ((prev := 1), (curr := 1))
    while True:  # noqa: WPS457
        prev, curr = curr, prev + curr
        yield curr


def fib_pair_gen() -> Generator[Tuple[int, int], None, None]:
    fib = fib_gen()
    tail = deque((next(fib),), maxlen=2)
    while True:
        tail.append(next(fib))
        yield (tail[0], tail[1])


def fib_phi_calc(precision: float) -> Tuple[int, int]:
    """
    Returns 2 consecutive Fibonacci numbers to calculate Golden Ratio with a
    given precision.
    """
    fpg = fib_pair_gen()
    while True:
        fib_pair = next(fpg)
        if abs(GOLDEN - fib_pair[1] / fib_pair[0]) <= precision:
            return fib_pair
