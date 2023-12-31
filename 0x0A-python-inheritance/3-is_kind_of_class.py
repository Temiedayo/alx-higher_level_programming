#!/usr/bin/python3
"""defines a class and inherited class-checking function."""


def is_kind_of_class(obj, a_class):
    """Scans if an object is an instance or inherited instance of a class.

    Args:
        obj (any): The object to be checked.
        a_class (type): The class
    Returns:
        If obj is an instance or inherited instance of a_class - True.
        Otherwise - False.
    """
    if isinstance(obj, a_class):
        return True
    return False
