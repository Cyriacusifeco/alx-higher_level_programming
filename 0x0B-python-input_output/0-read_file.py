#!/usr/bin/python3
"""initialize"""


def read_file(filename=""):
    """create function that read a text file"""
    with open(filename, encoding="UTF8") as f:

        print(f.read())
