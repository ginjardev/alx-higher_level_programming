#!/usr/bin/python3
"""This module appends given string to text file"""


def append_write(filename="", text=""):
    """Function appends string to text file

    Args:
        text (str): given string to append
    """
    with open(filename, mode='a', encoding='utf-8') as fp:
        return fp.write(text)