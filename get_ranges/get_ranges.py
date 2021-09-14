#!/usr/bin/env python

"""
Реализовать функцию `get_ranges` которая “сворачивает” список неповторяющихся
целых чисел, отсортированных по возрастанию:

- [0, 1, 2, 3, 4, 7, 8, 10] -> "0-4, 7-8, 10"
- [4, 7, 10] -> "4, 7, 10"
- [2, 3, 8, 9]) -> "2-3, 8-9"
"""
from itertools import islice
from typing import List


def get_ranges(seq: List[int]) -> str:
    if not seq:
        return ''
    ranges = []
    f_iter, c_iter = iter(seq), iter(seq)
    first = next(c_iter)
    for prev, curr in zip(f_iter, c_iter):
        if curr - prev == 1:
            continue
        range_ = format_range(first, prev)
        ranges.append(range_)
        first = curr
    range_ = format_range(first, curr)  # noqa: WPS441
    ranges.append(range_)
    return str.join(', ', ranges)


def format_range(first, last) -> str:
    if first == last:
        return f'{first}'  # noqa: WPS305
    return f'{first}-{last}'  # noqa: WPS305
