#!/usr/bin/python3
"""
5-hbtn_header.py
"""
import requests


if __name__ == "__main__":
    r = requests.get("https://alx-intranet.hbtn.io/status")
    print(r.headers['X-Request-Id'])
