#!/usr/bin/python3
"""
0-hbtn_status.py
"""
import urllib.request
from sys import argv


def main():
    """
    a Python script that fetches https://alx-intranet.hbtn.io/status
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
