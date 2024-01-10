#!/usr/bin/python3
"""This module writes string to a text file"""


def write_file(filename="", text=""):
    """Function writes given text to file
    Args:
        filename (object): file to write to
        text (str): string to write to text file
    """
    with open(filename, mode='w', encoding='utf-8') as fp:
        return fp.write(text)
