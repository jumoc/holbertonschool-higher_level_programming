#!/usr/bin/python3
"""hbtn status module"""
import requests
import sys
import json


if __name__ == "__main__":
    repository = sys.argv[1]
    name = sys.argv[2]
    url = "https://api.github.com/repos/{}/{}/commits".format(
        name, repository
    )
    r = requests.get(url)
    # with open("commits.json", "r", encoding="utf8") as file:
    #     f_json = json.loads(file.read())
    f_json = r.json()

    for i in range(10):
        print("{}: ".format(f_json[i].get('sha')), end="")
        print("{}".format(f_json[i].get('commit').get('author').get('name')))
