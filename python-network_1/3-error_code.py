#!/usr/bin/python3
"""
This script takes a URL as argument, sends a request to it,
and displays the response body or error code if an HTTPError occurs.
"""

import urllib.request
import urllib.error
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    req = urllib.request.Request(url)
    req.add_header('cfclearance', 'true')

    try:
        with urllib.request.urlopen(req) as response:
            body = response.read().decode('utf-8')
            print(body)
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
