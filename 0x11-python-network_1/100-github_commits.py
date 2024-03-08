#!/usr/bin/python3
"""
100-github_commits.py
"""
from sys import argv
import requests


if __name__ == "__main__":
    repo_name = argv[1]
    owner_name = argv[2]

    url = f"https://api.github.com/repos/{owner_name}/{repo_name}/commits"

    try:
        r = requests.get(url)
        res = r.json()
        for i in range(10):
            print("{}: {}".format(res[i]["sha"],
                                  res[i].get("commit").
                                  get("author").get("name")))
    except IndexError:
        pass
