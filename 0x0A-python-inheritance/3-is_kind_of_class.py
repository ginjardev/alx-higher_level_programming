#!/usr/bin/python3
""" Checks if obj is instance a class """


def is_kind_of_class(obj, a_class):
    """Checks if an object is an instance of a class

    Args:
      obj (object): Object to check.
      a_class: Class to check.

    Return:
      True if the object is instance of the class otherwise False
    """
    return isinstance(obj, a_class)
