#!/usr/bin/env python

"""
Напишите программу, которая рассчитывает расстояние Хэмминга(Hamming distance)
двух цепочек ДНК.

ДНК задаётся 4 нуклеотидами:

1. аденин - A 2. цитозин - C 3. гуанин - G 4. тимин - T

Расстояние Хэмминга оперделяет число отличающихся нуклеотидов, находящихся в
одинаковой позиции:

strand_a = GAGCCTACTAACGGGAT
strand_b = CATCGTAATGACGGCCT
           ^ ^ ^  ^ ^    ^^

Расстояние Хэмминга для данных цепочек = 7.
"""


def hamming_distance(strand_a: str, strand_b: str) -> int:
    if len(strand_a) != len(strand_b):
        raise ValueError('Цепочки ДНК должны быть одинаковой длины')
    return sum((1 for lt_a, lt_b in zip(strand_a, strand_b) if lt_a != lt_b))
