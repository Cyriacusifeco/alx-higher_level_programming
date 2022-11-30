#!/usr/bin/python3


def to_upper(str):

    new_str = ""

    if str == "":
        return str
    for character in str:
        asci = ord(character)
        if (asci >= 97) & (asci <= 122):
            new_str += chr(asci - 32)
        else:
            new_str += character
    return new_str


def uppercase(str):
    new_str = to_upper(str)
    print("{}".format(new_str))
