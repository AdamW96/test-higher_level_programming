#!/usr/bin/python3
"""
This script takes a URL as argument, sends a request to it using requests,
and displays the value of X-Request-Id header from the response.
"""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    headers = {
        'cfclearance': 'true'
    }

    response = requests.get(url, headers=headers)
    print(response.headers.get('X-Request-Id'))
