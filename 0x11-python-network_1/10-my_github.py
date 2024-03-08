#!/usr/bin/python3
"""
10-my_github.py
Write a Python script that takes your GitHub credentials
(username and password) and uses the GitHub API to display your id
"""
from sys import argv
import requests


if __name__ == "__main__":
    uname = argv[1]
    token = argv[2]

    url = "https://api.github.com/user"
    headers = {
        "Accept": "application/vnd.github+json",
        "Authorization": f"Bearer {token}",
        "X-GitHub-Api-Version": "2022-11-28"
    }
    try:
        r = requests.get(url, headers=headers)
        res = r.json()
        print(res.get("id"))
    except Exception:
        print(Exception)
