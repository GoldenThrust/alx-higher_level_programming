#!/usr/bin/python3
'''
    Take in URL and email param and  send POST 
    req to the URL with the email as param
    display the body of the response(decode: utf8)
'''

if __name__ == '__main__':
    import sys
    import urllib.request as ur
    import urllib.parse as up

    url = (sys.argv[1])
    eml = {'email': sys.argv[2]}

    data = up.urlencode(eml).encode('ascii')
    req = ur.Request(url, data)

    with ur.urlopen(req) as res:
        print(res.read().decode("utf-8"))
