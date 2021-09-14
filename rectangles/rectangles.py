#!/usr/bin/env python

"""
Даны два прямоугольника, стороны которых параллельны осям координат. Известны
координаты левого нижнего угла x, y, а также ширина и высота прямоугольника
w, h.

                w
    ┌───────────────────────┐
    │                       │
    │                       │ h
    │                       │
    └───────────────────────┘
 (x, y)

- определить, принадлежат ли все точки второго прямоугольника первому (`all`).
- определить, пересекаются ли эти прямоугольники (`any`, `all`).
"""
from collections import namedtuple

Rect = namedtuple('Rect', 'x y w h'.split())


def rect_inside(a: Rect, b: Rect) -> bool:
    """
    Checks if whole rectangle `b` is within rectangle `a`.
    """
    checker = get_bound_checker(a)
    return all(check_rect(b, checker))


def rects_intersect(a: Rect, b: Rect) -> bool:
    """
    Checks if 2 rectangles `a` and `b` have at least
    a single intersection point.
    """
    checker = get_bound_checker(a)
    return any(check_rect(b, checker))


def check_rect(rect, checker):
    return (checker(x, y)
            for x in (rect.x, rect.x + rect.w)
            for y in (rect.y, rect.y + rect.h)
            )


def get_bound_checker(rect):
    def point_checker(x, y):
        return all((
            rect.y <= y <= rect.y + rect.h,
            rect.x <= x <= rect.x + rect.w,
            ))
    return point_checker
