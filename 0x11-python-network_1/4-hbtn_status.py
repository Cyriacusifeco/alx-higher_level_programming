#!/usr/bin/python3
""" Fetches a given url using urlib """
import requests


if __name__ == '__main__':
    res = requests.get('https://alx-intranet.hbtn.io/status')
    print("Body response:")
    print("\t- type: {}\n\t- content: {}".format(type(res.text), res.text))
