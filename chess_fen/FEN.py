#!/usr/bin/env python

"""
Задача про шахматы.

Напишите программу, которая использует шахматную нотацию Форсайта-Эдвардса
(FEN - Forsyth–Edwards Notation) для подсчёта баланса материала между белыми
и чёрными.

- https://en.wikipedia.org/wiki/Forsyth–Edwards_Notation
- https://ru.wikipedia.org/wiki/Нотация_Форсайта_—_Эдвардса
- https://www.chessprogramming.org/Forsyth-Edwards_Notation

FEN задаёт полное расположение фигур на доске. Относительная ценность фигур
задана константами. Короли с доски не снимаются, поэтому учитывать их нет
смысла.

---

Добавьте функцию, которая возвращает строковое представление доски, например,
для начальной позиции:

```
r n b q k b n r
p p p p p p p p
· · · · · · · ·
· · · · · · · ·
· · · · · · · ·
· · · · · · · ·
P P P P P P P P
R N B Q K B N R
```
"""
from itertools import chain, cycle, islice
from typing import Generator

PAWN_VAL = 1  # пешка
KNIGHT_VAL = BISHOP_VAL = 3  # конь и слон  # noqa: WPS429
ROOK_VAL = 5  # ладья
QUEEN_VAL = 9  # ферзь

FREE_FLD = '□■'  # ·
SPACE = ' '
POS_KEYS = 'qkbnrp'
FIG_FORMS = dict(
    zip(
        POS_KEYS + POS_KEYS.upper(),
        '♛♚♝♞♜♟♕♔♗♘♖♙',
    ),
)

TRANSLATOR_DICT = dict(
    zip(
        POS_KEYS,
        (
            QUEEN_VAL,
            0,
            BISHOP_VAL,
            KNIGHT_VAL,
            ROOK_VAL,
            PAWN_VAL,
        ),
    ),
)


def calc_chess_balance(fen: str) -> int:
    score = 0
    for pos in fen:
        if pos == ' ':
            break
        pos_key = pos.lower()
        if pos_key not in TRANSLATOR_DICT:
            continue
        side_mul = -1 if pos.islower() else 1
        score += side_mul * TRANSLATOR_DICT[pos_key]
    return score


def chess_board(fen: str) -> str:
    board_gen = chess_board_gen(fen, '·', ' ')
    return str.join('', board_gen)


def chess_board_gen(  # noqa: WPS210, WPS231
    fen: str,
    field_mark: str = FREE_FLD,
    space: str = SPACE,
        ) -> Generator:
    """Genetate sequence of chess fields by FEN."""
    fields_gen = cycle(field_mark)
    space_gen = cycle((space,))
    fen_iter = iter(fen)
    prev_pos = next(fen_iter)
    for pos in fen_iter:
        is_eol = pos in '/ '
        if prev_pos.isdigit():
            rep_count = int(prev_pos)
            fields_seq = zip(islice(fields_gen, rep_count), space_gen)
            yield from traverse_iter(chain.from_iterable(fields_seq), is_eol)
        if prev_pos in FIG_FORMS:
            yield FIG_FORMS.get(prev_pos)
            if not is_eol:
                yield space
            next(fields_gen)
        if pos == '/':
            yield '\n'
            next(fields_gen)
        if pos == ' ':
            break
        prev_pos = pos


def traverse_iter(iterator, skip_last=False):
    prev = next(iterator)
    for elem in iterator:
        yield prev
        prev = elem
    if not skip_last:
        yield prev
