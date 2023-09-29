#!/usr/bin/python3
"""
    Takes in a letter and sends a POST request to
    http://0.0.0.0:5000/search_user with the letter as
    a parameter.
"""

if __name__ == '__main__':
    import sys
    import requests as r

    url = 'http://0.0.0.0:5000/search_user'
    urlArg = sys.argv[1] if sys.argv[1] else ''

    pRq = {'q': urlArg}

    urlR = r.post(url, data=pRq)

    try:
        res = urlR.json()

        if res == {}:
            print('No result')
        else:
            print('[{}] {}'.format(res.get('id'), res.get('name')))
    except ValueError:
        print('Not a valid JSON')
