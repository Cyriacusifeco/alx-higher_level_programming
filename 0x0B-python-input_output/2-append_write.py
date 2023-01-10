#!/usr/bin/python3
"""module"""


def append_write(filename="", text=""):
    """Appends a string at the end of a text file.

    Args:
        flename(str): Name of file
        text(str): string to append to file
    """

    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
