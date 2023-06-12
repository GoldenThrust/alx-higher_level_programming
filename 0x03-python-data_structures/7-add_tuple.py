#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    tup = tuple_a + (0, 0)
    tup2 = tuple_b + (0, 0)

    new_tuple = (tup[0] + tup2[0], tup[1] + tup2[1])
    return new_tuple
