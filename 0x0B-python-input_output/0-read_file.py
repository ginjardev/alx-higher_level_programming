#!/usr/bin/python3
"""Module with function to read file to STDOUT"""


def read_file(filename=""):
    """Function reads file
    Args:
        filename (object): file object
    """
    with open(filename, mode='r', encoding='utf-8') as fp:
        output = fp.read()
    print(output)
