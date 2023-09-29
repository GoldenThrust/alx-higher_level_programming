#!/usr/bin/python3
"""
    Takes GitHub credentials (username and password)
    and uses the GitHub API to display your id
"""

if __name__ == '__main__':
    import sys
    import requests as r
    from requests.auth import HTTPBasicAuth

    url = 'https://api.github.com/user'
    authe = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    res = r.get(url, auth=authe)

    rJson = res.json()
    print(rJson.get("id"))
