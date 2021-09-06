#!/usr/bin/env python

"""
Напишите программу, которая использует шахматную нотацию Форсайта-Эдвардса (FEN - Forsyth–Edwards Notation)
для подсчёта баланса материала между белыми и чёрными.

- https://en.wikipedia.org/wiki/Forsyth–Edwards_Notation
- https://ru.wikipedia.org/wiki/Нотация_Форсайта_—_Эдвардса
- https://www.chessprogramming.org/Forsyth-Edwards_Notation

FEN задаёт полное расположение фигур на доске.
Относительная ценность фигур задана константами.
Короли с доски не снимаются, поэтому учитывать их нет смысла.

---

Добавьте функцию, которая возвращает строковое представление доски, например, для начальной позиции:

```
r n b q k b n r
p p p p p p p p
. . . . . . . .
. . . . . . . .
. . . . . . . .
. . . . . . . .
p p p p p p p p
R N B Q K B N R
```
"""

PAWN_VAL = 1  # пешка
KNIGHT_VAL = BISHOP_VAL = 3  # конь и слон
ROOK_VAL = 5  # ладья
QUEEN_VAL = 9  # ферзь


def calc_chess_balance(fen: str) -> int:
    pass


def chess_board(fen: str) -> str:
    pass
