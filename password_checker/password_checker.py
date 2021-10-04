#!/usr/bin/env python

"""
Напишите функцию, которая проверяет "силу" пароля.

Надёжный пароль:
    - не менее 10 символов
    - содержит буквы разного регистра
    - минимум одну цифру
    - минимум один знак пунктуации
"""
from string import punctuation
from typing import Callable, Iterable

PASSWD_LENGTH_POLICY = 10


def is_strong_password(passwd: str) -> bool:
    """
    Check password strength using generators.

    My goal was checking by **one** loop ower password.
    I wrote special generators with locks for it.
    """
    if len(passwd) < PASSWD_LENGTH_POLICY:
        return False
    checkers = (
        get_has_digit_it(passwd),
        get_has_punctuation_it(passwd),
        get_has_not_unicase_it(passwd),
        )
    for _ in passwd:
        flags = map(next, checkers)
        if all(flags):
            return True
    return False


def get_has_not_unicase_it(passwd):
    fl_not_unicase = False
    prev_is_upper = passwd[0].isupper()
    yield False
    for curr_char in passwd[1:]:
        if curr_char.isalpha():
            curr_is_upper = curr_char.isupper()
            fl_not_unicase = (curr_is_upper != prev_is_upper)
            prev_is_upper = curr_is_upper
        if fl_not_unicase:
            break
        yield False
    while True:  # noqa: WPS457
        yield fl_not_unicase


def get_has_punctuation_it(passwd):
    fl_punctuation = False
    for curr_char in passwd:
        fl_punctuation = curr_char in punctuation
        if fl_punctuation:
            break
    while True:  # noqa: WPS457
        yield fl_punctuation


def get_has_digit_it(passwd):
    fl_digit = False
    for curr_char in passwd:
        fl_digit = curr_char.isdigit()
        if fl_digit:
            break
    while True:  # noqa: WPS457
        yield fl_digit
