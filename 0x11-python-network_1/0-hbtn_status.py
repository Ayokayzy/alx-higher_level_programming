#!/usr/bin/python3
"""
0-hbtn_status.py
"""
import urllib.request


def main():
    """
    a Python script that fetches https://alx-intranet.hbtn.io/status
    """

    req = urllib.request.Request(
        "https://alx-intranet.hbtn.io/status")
    with urllib.request.urlopen(req) as response:
        status = response.read()
        res = "Body response:\n\
\t- type: {}\n\
\t- content: {}\n\
\t- utf8 content: {}".format(type(response.read()), status, response.msg)
        print(res)


if __name__ == "__main__":
    main()
