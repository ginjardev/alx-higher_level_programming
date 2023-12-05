#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    tuple_a += (0,0)
    tuple_b += (0,0)
    tuple_c =  (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
    return tuple_c


if __name__ == "__main__":
    add_tuple(tuple_a=(), tuple_b=())
