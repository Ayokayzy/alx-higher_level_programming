#!/usr/bin/python3
"""
4-hbtn_status.py
"""
import requests


if __name__ == "__main__":
    r = requests.get("https://alx-intranet.hbtn.io/status")
    print("Body response:")
    print("    - type: {}".format(type(r.text)))
    print("    - content: {}".format(r.text))
