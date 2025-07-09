#!/usr/bin/python3
"""
This script fetches https://intranet.hbtn.io/status using requests
and displays the body response information.
"""

import requests

if __name__ == "__main__":
    headers = {
        'User-Agent': 'Mozilla/5.0',
        'cfclearance': 'true'
    }

    response = requests.get('https://intranet.hbtn.io/status', headers=headers)
    content = response.text

    print("Body response:")
    print("\t- type: {}".format(type(content)))
    print("\t- content: {}".format(content))
