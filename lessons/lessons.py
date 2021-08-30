#!/usr/bin/env python

"""
Задача про окончание уроков.

В школе, в которой учится В. Пупкин, занятия начинаются в 8 утра.
Урок длится 45 минут.
После каждого нечётного урока (1-го, 3-го, 5-го ...) перемена 5 минут,
а после каждого чётного (2-го, 4-го, 6-го ...) - 15.

Помогите непоседе Васе посчитать, когда заканчивается n-ый урок.
"""
import sys
from typing import Tuple

STARTING_MINUTE = 8 * 60
MINUTES_IN_DAY = 24 * 60
LESSON_MINS = 45
EVEN_ODD_GAP_MINS = 15
ODD_EVEN_GAP_MINS = 5


def end_of_lesson(lessons_amount: int) -> Tuple[int, int]:
    """Chech for parameter sanity and return result."""
    if lessons_amount <= 0:
        raise ValueError(
            f"Illegal lessons amount ({lessons_amount})")
    hours, minutes = end_of_lesson_calc(lessons_amount)
    if hours * 60 + minutes > MINUTES_IN_DAY:
        raise ValueError(
            f"To many lessons amount for 1 day ({lessons_amount})")
    return (hours, minutes)


def end_of_lesson_calc(lessons_amount: int) -> Tuple[int, int]:
    """Calculate todays end of lessons session."""
    lessons_duration = LESSON_MINS * lessons_amount
    even_odd_gaps, odds_rem = divmod(lessons_amount - 1, 2)
    odd_even_gaps_duration = (even_odd_gaps + odds_rem) * ODD_EVEN_GAP_MINS
    even_odd_gaps_duration = even_odd_gaps * EVEN_ODD_GAP_MINS
    gaps_duration = odd_even_gaps_duration + even_odd_gaps_duration
    ends_minute = STARTING_MINUTE + lessons_duration + gaps_duration
    return divmod(ends_minute, 60)


if __name__ == "__main__":
    try:
        last_lesson_number = int(input("Введите номер последнего урока: "))
    except Exception as e:
        print(e)
        sys.exit(1)

    try:
        hours, minutes = end_of_lesson(last_lesson_number)
    except ValueError as e:
        print(f"Недопустимое количество уроков ({last_lesson_number}). {e}")
        sys.exit(1)

    print(f"{last_lesson_number}-ый урок заканчивается в {hours}:{minutes:02}")
