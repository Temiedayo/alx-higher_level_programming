#!/usr/bin/python3
"""defines a Python class-to-JSON function."""


def class_to_json(obj):
    """return dictionary representation of a simple data structure."""
    return obj.__dict__
