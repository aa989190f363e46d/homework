#!/usr/bin/env python
"""
 Бабушка Зина любит печь блины своему любимому внуку Васе. А внук Вася любит
 математику и знает, что периметр и площадь блина можно найти по диаметру
 сковородки. Напишите программу, которая поможет Васе проверить его
 вычисления.
"""
import sys
from math import pi


def check_diameter_value(diameter):
    if diameter < 0:
        raise ValueError(f"Negative diameter ({diameter}) is invalid")


def perimeter(diameter):
    check_diameter_value(diameter)
    return pi * diameter


def aria(diameter):
    check_diameter_value(diameter)
    raduis = diameter / 2
    return pi * pow(raduis, 2)


if __name__ == "__main__":
    d = int(input("Диаметр сковороды = "))

    try:
        pan_perimeter = perimeter(d)
    except ValueError as e:
        print(e)
        sys.exit(1)

    print(f"Периметр сковороды:\t{pan_perimeter:>10.2f} ед")

    pan_aria = aria(d)
    print(f"Площадь сковороды: \t{pan_aria:>10.2f} кв. ед")
