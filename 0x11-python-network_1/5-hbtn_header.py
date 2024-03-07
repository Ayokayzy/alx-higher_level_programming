#!/usr/bin/python3
"""
5-hbtn_header.py
"""
import requests
from sys import argv


if __name__ == "__main__":
    if (len(argv) == 2):
        r = requests.get(argv[1])
        print(r.headers.get('X-Request-Id'))
