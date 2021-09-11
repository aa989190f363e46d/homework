#!/usr/bin/env python

"""
Рисует.
"""

import sys
import turtle

from polygon import get_polygon_vertices


RADIUS = 200.0
PENSIZE = 10


if __name__ == "__main__":
    if len(sys.argv) > 1:
        n_vert = int(sys.argv[1])
    else:
        n_vert = 6  # draw hexagon by default
        # n_vert = int(input("Vertexes amount = "))  # or read from stdin

    vertices_gen = get_polygon_vertices(n_vert, RADIUS)

    # setup
    rafael = turtle.Turtle()
    rafael.color('magenta', 'darkolivegreen3')
    rafael.pensize(PENSIZE)

    # go to first vertex
    start_point = next(vertices_gen)
    rafael.penup()
    rafael.goto(*start_point)
    rafael.pendown()

    # draw polygon
    rafael.begin_fill()
    for point in vertices_gen:
        rafael.goto(*point)

    # go to initial vertex to finish the shape
    rafael.goto(*start_point)
    rafael.end_fill()

    # done
    turtle.exitonclick()
