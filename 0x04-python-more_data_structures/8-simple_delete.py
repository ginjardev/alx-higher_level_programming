#!/usr/bin/python3


def simple_delete(a_dictionary, key=""):
    a_dictionary.pop(key, "default")
    return a_dictionary


if __name__ == "__main__":
    simple_delete(a_dictionary, key="")
