#!/usr/bin/python3
'''
    Fetches: https://alx-intranet.hbtn.io/status
    and display the type, content and content in utf8 format.
'''

if __name__ == '__main__':
    import urllib.request as ur

    with ur.urlopen('https://alx-intranet.hbtn.io/status') as res:
        response = res.read()
        print("Body response:")
        print("\t- type: {}".format(type(response)))
        print("\t- content: {}".format(response))
        print("\t- utf8 content: {}".format(response.decode('utf-8')))
