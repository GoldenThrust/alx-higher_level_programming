#!/usr/bin/python3
'''
    takes in a URL, sends a request to the URL
    and displays the body of the response (decoded in utf-8)
'''

if __name__ == '__main__':
    import sys
    import urllib.request as ur
    import urllib.error as ue

    url = (sys.argv[1])

    req = ur.Request(url)

    try:
        with ur.urlopen(req) as res:
            print(res.read().decode("utf-8"))
    except ue.HTTPError as err:
        print('Error code: {}'.format(err.code))
