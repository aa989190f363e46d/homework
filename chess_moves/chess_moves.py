#!/usr/bin/env python

"""
Напишите функции для вывода ходов шахматных фигур на пустой доске.

Например, для коня на поле a1 доступных полей будет 2: b3 и с2,
а для ладьи на поле a1 будут доступны вся вертикаль a и 1-ая горизонталь.
"""
from itertools import chain, starmap
from string import ascii_lowercase
from typing import List, Tuple

BOARD_SIZE = 8
HORIZ_LINE = ascii_lowercase[:BOARD_SIZE]
VERT_LINE = list(map(str, range(1, BOARD_SIZE + 1)))


def rook_moves(square: str) -> List[str]:
    horiz, vert = split_position_into_coord(square)
    turns_vars = get_cross(horiz, vert)
    return list(turns_vars)


def bishop_moves(square: str) -> List[str]:
    horiz, vert = split_position_into_coord(square)
    turns_vars = chain(
        get_top_diag(horiz, vert),
        get_low_diag(horiz, vert),
        )
    return list(turns_vars)


def queen_moves(square: str) -> List[str]:
    horiz, vert = split_position_into_coord(square)
    turns_vars = chain(
        get_cross(horiz, vert),
        get_top_diag(horiz, vert),
        get_low_diag(horiz, vert),
        )
    return list(turns_vars)


def knight_moves(square: str) -> List[str]:
    horiz, vert = split_position_into_coord(square)
    h_ranges = (
        range(horiz - min(horiz, 2), horiz),
        range(horiz + 1, horiz + min(BOARD_SIZE - horiz - 1, 2) + 1),
        )
    v_ranges = (
        range(vert - min(vert, 2), vert),
        range(vert + 1, vert + min(BOARD_SIZE - vert - 1, 2) + 1),
        )
    h_ranges_full = chain(h_ranges, map(reversed, h_ranges))
    v_ranges_full = chain(*zip(map(reversed, v_ranges), v_ranges))
    points = chain(*starmap(zip, zip(h_ranges_full, v_ranges_full)))
    turns_vars = starmap(build_position, points)
    return list(turns_vars)


def king_moves(square: str) -> List[str]:
    horiz, vert = split_position_into_coord(square)
    turns_vars = chain(
        get_cross(horiz, vert, 1),
        get_top_diag(horiz, vert, 1),
        get_low_diag(horiz, vert, 1),
        )
    return list(turns_vars)


def split_position_into_coord(positon: str) -> Tuple[int, int]:
    horiz, vert = tuple(positon)
    return HORIZ_LINE.index(horiz), VERT_LINE.index(vert)


def build_position(horiz, vert) -> str:
    return f'{HORIZ_LINE[horiz]}{VERT_LINE[vert]}'


def get_low_diag(horiz: int, vert: int, rng: int = BOARD_SIZE) -> starmap:
    offset = min(horiz, vert, rng)
    horiz_vars = chain(
        range(horiz - offset, horiz),
        range(horiz + 1, min(horiz + rng + 1, BOARD_SIZE)),
        )
    vert_vars = chain(
        range(vert - offset, vert),
        range(vert + 1, min(vert + rng + 1, BOARD_SIZE)),
        )
    return starmap(build_position, zip(horiz_vars, vert_vars))


def get_top_diag(horiz: int, vert: int, rng: int = BOARD_SIZE) -> starmap:
    offset = min(horiz, abs(rng - vert - 1), rng)
    horiz_vars = chain(
        range(horiz - offset, horiz),
        range(horiz + 1, min(horiz + rng + 1, BOARD_SIZE)),
        )
    vert_vars = chain(
        range(vert + offset, vert, -1),
        range(vert - 1, max(vert - rng - 1, -1), -1),  # noqa: WPS221
        )
    return starmap(build_position, zip(horiz_vars, vert_vars))


def get_cross(horiz: int, vert: int, rng: int = BOARD_SIZE) -> starmap:
    offset_h, offset_v = min(horiz, rng), min(vert, rng)
    horiz_vars = chain(
        range(horiz - offset_h, horiz),
        range(horiz + 1, min(horiz + rng + 1, BOARD_SIZE)),
        )
    vert_vars = chain(
        range(vert - offset_v, vert),
        range(vert + 1, min(vert + rng + 1, BOARD_SIZE)),
        )
    return starmap(build_position,
                   chain(
                        ((hor, vert) for hor in horiz_vars),
                        ((horiz, ver) for ver in vert_vars),
                        ))
