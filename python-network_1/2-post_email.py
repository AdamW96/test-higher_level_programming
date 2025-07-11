#!/usr/bin/python3
"""
This script takes a URL and an email as arguments, sends a POST request
to the URL with the email as a parameter, and displays the response body.
"""

import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    data = urllib.parse.urlencode({'email': email}).encode('utf-8')
    req = urllib.request.Request(url, data=data, method='POST')
    req.add_header('cfclearance', 'true')

    with urllib.request.urlopen(req) as response:
        body = response.read().decode('utf-8')
        print(body)
