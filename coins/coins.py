#!/usr/bin/env python
"""
Бабушка Зина даёт своему любимому внуку Васе 3 монеты и разрешает оставить 2
из них. Найдите максимальную сумму из любых двух монет. Номинальная стоимость
монет: a, b и с тугриков.
"""
from typing import List
import sys


def max_sum_of_2(*args) -> int:
    if len(args) != 3:
        raise ValueError(f"Count of arguments must be 3 but get {len(args)}")
    for coin_val in args:
        try:
            check_coin_val(coin_val)
        except ValueError as e:
            raise e
    return _calculate_sum(*args)


def check_coin_val(coin_val: int) -> None:
    if not type(coin_val) == int:
        raise ValueError(f"Illegal coin value type ({coin_val})")
    if coin_val <= 0:
        raise ValueError(f"Illegal coin nominal ({coin_val})")


def _calculate_sum(*args):
    return sum(sorted(args)[-2:])


def get_coin_input(coin_name: str) -> int:
    suggest = f"Введите номинал монеты {coin_name}: "
    coin_inp = input(suggest)
    try:
        coin_val = int(coin_inp)
    except ValueError as e:
        raise ValueError(f"Wrong input ({coin_inp}). Causes error: {e}")
    return coin_val


if __name__ == "__main__":
    coins: List[int] = []
    for num, _ in enumerate(range(3), 1):
        try:
            coin_val = get_coin_input(f"{num}")
        except ValueError as e:
            print(f"Error: {e}")
            sys.exit(1)
        coins.append(coin_val)

    try:
        max_sum = max_sum_of_2(*coins)
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)

    print(f"Вася оставит себе {max_sum}₮.")
