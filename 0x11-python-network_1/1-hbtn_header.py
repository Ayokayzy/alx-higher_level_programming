#!/usr/bin/python3
"""
1-hbtn_header.py
"""
import urllib.request
from sys import argv


def main():
    """
    Write a Python script that takes in a URL, sends a request
    to the URL and displays the value of the X-Request-Id
    variable found in the header of the response.
    """

    req = urllib.request.Request(argv[1])
    try:
        with urllib.request.urlopen(req) as response:
            res = response.read()
            print(response.headers["X-Request-Id"])

    except Exception:
        pass


if __name__ == "__main__":
    main()
