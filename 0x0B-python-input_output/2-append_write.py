#!/usr/bin/python3
"""Defines file-appending function."""


def append_write(filename="", text=""):
    """appends a string to the end of a UTF8 text file.

    Args:
        filename (str): name of the file to be appended to.
        text (str): string to be appended to the file.
    Returns:
        The num of chars appended.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
