#!/usr/bin/python3
"""This module returns the dictionary description for JSON serialization"""


def class_to_json(obj):
    """Function returns object dict for JSON serialization

    Args:
        obj (object): an object instance
    """
    return obj.__dict__
