#!/usr/bin/env python

"""
В. Пупкин развозит пиццу. Ему сообщают адрес доствки в виде <улица> <номер
дома>-<номер квартиры>

Приезжая по указанному адресу, Вася видит f-этажное здание. Для простоты будем
считать, что на каждом этаже в подъезде находятся 4 квартиры.

Помогите Васе посчитать, в каком подъезде и на каком этаже находится нужная
квартира n.

Для решения понадобится использовать деление по модулю % или целочисленное
деление //.
"""
from math import ceil

FLATS_PER_FLOOR = 4


def check_buildig_height(building_height):
    if building_height <= 0:
        raise ValueError(
            f"Negative or zero height ({building_height}) is invalid"
            )


def check_flat_num(flat_num):
    if flat_num <= 0:
        raise ValueError(
            f"Negative or zero apartaments number ({flat_num}) is invalid"
            )


def flats_per_entrance(building_height):
    return FLATS_PER_FLOOR * building_height


def find_entrance(building_height, flat_num):
    """
    building_height - число этажей в доме
    flat_num        - номер квартиры
    """
    check_buildig_height(building_height)
    check_flat_num(flat_num)
    return ceil(flat_num / flats_per_entrance(building_height))


def find_floor(building_height, flat_num):
    """
    building_height - число этажей в доме
    flat_num        - номер квартиры
    """
    check_buildig_height(building_height)
    check_flat_num(flat_num)
    flat_num_in_ent = flat_num % flats_per_entrance(building_height)
    if flat_num_in_ent == 0:
        return building_height
    return ceil(flat_num_in_ent / FLATS_PER_FLOOR)


if __name__ == "__main__":
    import sys

    try:
        inp_floors = input("Число этажей: ")
        floors = int(inp_floors)
    except ValueError as e:
        print(f"Invalid input floors={inp_floors}", e, sep="\n")
        sys.exit(1)

    try:
        inp_flat_num = input("Номер квартиры: ")
        flat_num = int(inp_flat_num)
    except ValueError as e:
        print(f"Invalid input flat_num={inp_flat_num}", e, sep="\n")
        sys.exit(1)

    try:
        entrance = find_entrance(floors, flat_num)
    except ValueError as e:
        print(e)
        sys.exit(1)

    ent_floor = find_floor(floors, flat_num)

    print("\nВасилий, для выполнения заказа проследуйте")
    print(f"к подъезду\t№{entrance:>4}")
    print(f"на этаж\t\t№{ent_floor:>4}")
