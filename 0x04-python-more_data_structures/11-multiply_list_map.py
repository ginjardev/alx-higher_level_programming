#!/usr/bin/python3


def multiply_list_map(my_list=[], number=0):
    result = list(map(lambda x: x * number, my_list))
    return result


if __name__ == "__name__":
    multiply_list_map(my_list=[], number=0)
