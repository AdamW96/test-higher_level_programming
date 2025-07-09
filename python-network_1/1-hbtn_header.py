#!/usr/bin/python3
"""
This script takes a URL as argument, sends a request to it,
and displays the value of X-Request-Id header from the response.
"""

import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    req = urllib.request.Request(url)
    req.add_header('cfclearance', 'true')
    with urllib.request.urlopen(req) as response:
        print(response.getheader('X-Request-Id'))
