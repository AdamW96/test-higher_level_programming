#!/bin/bash
# This script sends an OPTIONS request to a URL and displays all HTTP methods the server will accept
curl -s -X OPTIONS "$1" -I | grep "Allow:" | cut -d' ' -f2-