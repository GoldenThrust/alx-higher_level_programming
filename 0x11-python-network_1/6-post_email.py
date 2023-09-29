#!/usr/bin/python3
'''
    Takes in a URL and an email address,
    sends a POST request to the passed URL
    with the email as a parameter, and finally
    displays the body of the response
'''

if __name__ == '__main__':
    import sys
    import requests as r

    url = sys.argv[1]
    emval = {'email': sys.argv[2]}
    urlB = r.post(url, data=emval)

    print(urlB.text)
