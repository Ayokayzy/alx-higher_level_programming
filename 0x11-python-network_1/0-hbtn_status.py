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
    try:
        with urllib.request.urlopen(req) as response:
            status = response.read()
            res = "Body response:\n\
\t- type: {}\n\
\t- content: {}\n\
\t- utf8 content: {}".format(type(status), status, status.decode('utf-8'))
            print(res)
    except Exception:
        pass


if __name__ == "__main__":
    main()
