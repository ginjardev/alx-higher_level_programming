#!/usr/bin/python3
"""Lookup Module - Lists available attributes and methods of an object"""

def lookup(obj):
    """List attributes of an object
    
    Args:
        obj (object): object instance of a class

    Returns: list of attributes
    """
    return dir(obj)
