#!/usr/bin/python3
"""defines a class-checking function."""


def is_same_class(obj, a_class):
    """Scans if an object is exactly an instance of a given class.

    Args:
        obj (any): The object to be checked.
        a_class (type): The class
    Returns:
        If obj is exactly an instance of a_class - True.
        Otherwise - False.
    """
    if type(obj) == a_class:
        return True
    return False
