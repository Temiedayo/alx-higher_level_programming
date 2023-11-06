#!/usr/bin/python3
"""defines an inherited list class MyList."""


class MyList(list):
    """implements sorted outputing for the built-in list class."""

    def print_sorted(self):
        """output a list in sorted ascending order."""
        print(sorted(self))
