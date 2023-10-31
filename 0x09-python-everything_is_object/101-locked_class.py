#!/usr/bin/python3
"""defines locked class."""

class LockedClass:
    """
    Avert user from instantiating new LockedClass attributes
    for anything but attributes called 'first_name'.
    """

    __slots__ = ["first_name"]
