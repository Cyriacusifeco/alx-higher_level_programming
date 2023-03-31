#!/usr/bin/python3
""" Fetches a given url using urlib """
import urllib.request


if __name__ == '__main__':
    url = 'https://alx-intranet.hbtn.io/status'
    with urllib.request.urlopen(url) as response:
        content = response.read()
        print("Body response:")
        print("\t- type: {}\n\t- content: {}\n\t- utf8 content: {}".format(
            type(content), content,
            content.decode('utf-8')))
