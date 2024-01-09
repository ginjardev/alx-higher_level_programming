#!/usr/bin/python3

"""checks if object is instance of a class"""

def is_same_class(obj, a_class):
    """checks if object is instance of class

    Args:
        obj (object): object of Python class 
        a_class (class): custom Python class

    Returns:
        True if obj is instance otherwise False
    """
    return type(obj) == a_class