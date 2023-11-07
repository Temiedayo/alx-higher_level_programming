#!/usr/bin/python3
"""defines file-writing function."""


def write_file(filename="", text=""):
    """Write string to a UTF8 text file.

    Args:
        filename (str): name of the file to be written.
        text (str): The text to be written to the file.
    Returns:
        The num of chars written.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
