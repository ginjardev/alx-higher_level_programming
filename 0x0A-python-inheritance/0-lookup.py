#!/usr/bin/python3
"""Lists available attributes and methods of an object"""

def lookup(obj):
    """List attributes of an object
    Args:
        obj: object instance of a class
    Returns: list of attributes
    """
    return dir(obj)
