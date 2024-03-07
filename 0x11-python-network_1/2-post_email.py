#!/usr/bin/python3
"""
2-post_email.py
"""
from sys import argv
from urllib import request, parse


def main():
    url = argv[1]
    values = {'email': argv[2]}

    data = parse.urlencode(values).encode('ascii')
    req =  request.Request(url, data)
    try:
        with request.urlopen(req) as response:
            page = response.read()
            print(page.decode('utf-8'))
    except Exception:
        print(Exception)


if __name__ == "__main__":
    main()
