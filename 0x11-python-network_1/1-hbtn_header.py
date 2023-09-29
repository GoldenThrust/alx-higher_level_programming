#!/usr/bin/python3
'''
    Takes in parameter and display
    the value of the X-Request-Id variable found
    in the header of the response.
'''

if __name__ == '__main__':
    import sys
    import urllib.request as ur

    with ur.urlopen(sys.argv[1]) as res:
        response = res.header
        print(dict(response).get('X-Request-Id'))
