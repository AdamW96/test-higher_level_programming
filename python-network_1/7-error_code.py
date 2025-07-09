#!/usr/bin/python3
"""
This script takes a URL as argument, sends a request to it using requests,
and displays the response body or error code if status code >= 400.
"""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    response = requests.get(url)

    if response.status_code >= 400:
        print("Error code: {}".format(response.status_code))
    else:
        print(response.text)
