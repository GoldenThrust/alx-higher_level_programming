#!/usr/bin/python3
'''
    Takes in a URL, sends a request to the URL
    and displays the body of the response.
'''

if __name__ == '__main__':
    import sys
    import requests as r

    url = sys.argv[1]
    urlB = r.get(url)

    if urlB.status_code >= 400:
        print('Error code: {}'.format(urlB.status_code))
    else:
        print(urlB.text)
