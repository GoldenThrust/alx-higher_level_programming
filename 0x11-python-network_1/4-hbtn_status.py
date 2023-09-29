#!/usr/bin/python3
'''
    Fetches https://alx-intranet.hbtn.io/status
'''

if __name__ == '__main__':
    import requests as r

    url = 'https://alx-intranet.hbtn.io/status'
    urlB = r.get(url)

    print("Body response:")
    print("\t- type: {}".format(type(urlB.text)))
    print("\t- content: {}".format(urlB.text))
