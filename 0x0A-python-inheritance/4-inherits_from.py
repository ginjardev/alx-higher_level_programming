#!/usr/bin/python3
""" Checks if obj is instance of a class inherited (directly or indirectly) """


def inherits_from(obj, a_class):
    """Checks if an object is instance of a class (directly or indirectly)

    Args:
      obj (object): Object to check.
      a_class: Class to check.

    Return:
      True if the object is instance of the class False otherwise
    """
    return isinstance(obj, issubclass(type(obj), a_class))
