#!/usr/bin/python3
"""writes to text file"""


def write_file(filename="", text=""):
    """Writes a string to a text file (UTF-8).

    Args:
        filename(str): The name of file
        text(str): String to write to file
    """

    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
