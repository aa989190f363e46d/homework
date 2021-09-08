#!/usr/bin/env python

"""
Напишите программу, которая кодирует и декодирует текст шифром Атбаш. В этом
шифре каждая i-ая буква алфавита заменяется i-ой буквой с его конца,
например, для латинского алфавита: a - z, b - y и т.д.

- заглавные буквы переводятся в строчные
- пробельные символы и знаки препинания опускаются
- шифр идёт блоками по 5 символов, между ними пробел

Пример:

`Bambarbia, Kirgudu` -> `yznyz iyrzp ritfw f`
"""
from string import ascii_letters
from typing import Generator

BLOCK_SIZE = 5

TRANS = str.maketrans(
    ascii_letters[:26],  # noqa: WPS432
    str.join('', reversed(ascii_letters[:26])),  # noqa: WPS432
    )


def atbash_encode(text: str) -> str:
    encode_gen = atbash_encode_gen(text)
    return str.join(' ', encode_gen)


def atbash_encode_gen(text: str) -> Generator:
    text_iter = filter(filter_predicate, map(str.lower, text))
    chunk_iter = (iter(text_iter),) * BLOCK_SIZE
    while True:
        chunk = str.join('', map(next, chunk_iter))
        if not chunk:
            break
        yield translator(chunk)


def atbash_decode(cipher: str) -> str:
    return str.translate(str.replace(cipher, ' ', ''), TRANS)


def translator(char: str) -> str:
    return str.translate(char, TRANS)


def filter_predicate(char):
    return str.isalpha(char) or str.isnumeric(char)
