#!/usr/bin/python3
"""
This script fetches https://intranet.hbtn.io/status using urllib
and displays the body response information.
"""

import urllib.request

if __name__ == "__main__":
    req = urllib.request.Request('https://intranet.hbtn.io/status')
    req.add_header('cfclearance', 'true')
    with urllib.request.urlopen(req) as response:
        body = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(body)))
        print("\t- content: {}".format(body))
        print("\t- utf8 content: {}".format(body.decode('utf-8')))
