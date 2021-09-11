#!/usr/bin/env python

""" Напишите функцию, которая генерирует вершины n-угольника.

Функция возвращает список вершин. Каждая вершина задаётся таплом из координат
x и y. Первая вершина лежит на оси Y: `(0.0, R)` (т.е. на 12 часов),
следующие идут по часовой стрелке.

Например, квадрат будет иметь следующие 4 вершины:

`[(0.0, R), (R, 0.0), (0.0, -R), (-R, 0.0)]`

```
        y
        ↑
        1
       ╱┼╲
      ╱ ┼ ╲
    ─4┼┼┼┼┼2─→x
      ╲ ┼ ╱
       ╲┼╱
        3
        │
```

«Вращать» будем через умножение компле́ксных чисел:
- https://www.cuemath.com/jee/rotation-complex-numbers/
"""
import math
from typing import Generator

RADIUS = 3.0


def polygon_vertices(n_vert: int, rad: float = RADIUS) -> list:
    vert_gen = get_polygon_vertices(n_vert, rad)
    return list(vert_gen)


def get_polygon_vertices(n_vert: int, rad: float = RADIUS) -> Generator:
    start_z = complex(0, rad)
    arc_gen = get_arc_generator(n_vert, start_z)

    start_point = compl_to_tuple(start_z)
    yield start_point

    right_half_arc = []
    half, h_rem = divmod(n_vert, 2)
    quart, q_rem = divmod(half, 2)
    q_mid_point = quart + q_rem
    for _ in range(1, q_mid_point):
        point = next(arc_gen)
        right_half_arc.append(point)
        yield point
    if h_rem == 0:
        u_bound = None
        if q_rem == 0:
            u_bound = -1
            point = tuple(start_point[::-1])
            right_half_arc.append(point)
            yield point
        for q_arc_point in reversed(right_half_arc[:u_bound]):
            point = reflect_point_down(q_arc_point)
            right_half_arc.append(point)
            yield point
        yield reflect_point_down(start_point)
    else:
        mid_point = half + h_rem
        for _ in range(q_mid_point, mid_point):
            point = next(arc_gen)
            right_half_arc.append(point)
            yield point
    yield from map(reflect_point_left, reversed(right_half_arc))


def get_arc_generator(n_vert, start_point):
    rot_angle_deg = 360 / n_vert
    rot_power = complex(0, 1) * math.radians(rot_angle_deg)
    rot_factor = math.e ** rot_power
    prev_point = start_point
    while True:
        prev_point /= rot_factor
        yield compl_to_tuple(prev_point)


def compl_to_tuple(z: complex) -> tuple:
    return (z.real, z.imag)


def reflect_point_left(point):
    return (-point[0], point[1])


def reflect_point_down(point):
    return (point[0], -point[1])
