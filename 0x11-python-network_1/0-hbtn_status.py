#!/usr/bin/python3
"""initializate"""
from urllib.request import urlopen


def alx_status_0():
    """function show my status"""
    with urlopen('https://intranet.hbtn.io/status') as response:
        page = response.read()
        utf8 = page.decode('utf-8')
        print("Body response:\n\t- type: {}".format(type(page)))
        print("\t- content: {}\n\t- utf8 content: {}".
              format(page, utf8, end=""))


if __name__ == '__main__':
    alx_status_0()
