#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    if tuple_a is None or tuple_b is None:
        return
    tuple_a += (0,0)
    tuple_b += (0,0)
    return (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])


if __name__ == "__main__":
    add_tuple(tuple_a=(), tuple_b=())
