#!/usr/bin/python3
"""
    Takes GitHub credentials (username and password)
    and uses the GitHub API to display your id
"""

if __name__ == '__main__':
    import sys
    import requests as r

    url = "https://api.github.com/repos/{}/{}/commits".format(
                    sys.argv[2], sys.argv[1])

    res = r.get(url)

    coms = res.json()

    try:
        for i in range(10):
            print("{}: {}".format(
                  coms[i].get("sha"),
                  coms[i].get("commit")
                  .get("author").get("name")))
    except IndexError:
        pass
