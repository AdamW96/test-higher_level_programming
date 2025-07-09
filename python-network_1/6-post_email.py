#!/usr/bin/python3
"""
This script takes a URL and an email as arguments, sends a POST request
to the URL with the email as a parameter using requests, and displays the response body.
"""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    headers = {
        'cfclearance': 'true'
    }

    data = {'email': email}
    response = requests.post(url, data=data, headers=headers)
    print(response.text)
