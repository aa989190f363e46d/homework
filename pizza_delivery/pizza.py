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


def flats_per_entrance(building_height):
    return FLATS_PER_FLOOR * building_height


def find_entrance(building_height, apart_num):
    """
    building_height - число этажей в доме
    apart_num       - номер квартиры
    """
    return ceil(apart_num / flats_per_entrance(building_height))


def find_floor(building_height, apart_num):
    """
    building_height - число этажей в доме
    apart_num       - номер квартиры
    """
    apart_num_in_ent = apart_num % flats_per_entrance(building_height)
    if apart_num_in_ent == 0:
        return building_height
    return ceil(apart_num_in_ent / FLATS_PER_FLOOR)


if __name__ == "__main__":
    floors = int(input("Число этажей: "))
    flat_num = int(input("Номер квартиры: "))

    entrance = find_entrance(floors, flat_num)
    ent_floor = find_floor(floors, flat_num)
    print(entrance, ent_floor)
