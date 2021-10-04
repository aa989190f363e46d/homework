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
    Check password strength using filters.

    Simple, bit, i think (really not (: ),
    it must be not very effective, because
    each filter starts from 1'st symbol.
    """
    if len(passwd) < PASSWD_LENGTH_POLICY:
        return False

    def build_filter(  # noqa: WPS430
            checker: Callable[[str], bool],
            ) -> Iterable[str]:
        return filter(checker, passwd)

    bariers = (
        str.isdigit,
        str.isupper,
        str.islower,
        is_punctuation,
        )

    for flt in map(build_filter, bariers):
        try:
            next(flt)  # type: ignore[call-overload]
        except StopIteration:
            return False

    return True


def is_punctuation(char: str) -> bool:
    return char in punctuation
