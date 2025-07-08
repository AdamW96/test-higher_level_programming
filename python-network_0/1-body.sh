#!/bin/bash
# This script sends a GET request to a URL and displays the body only for 200 status code responses
curl -s -w "%{http_code}" "$1" | grep -E "200$" | sed 's/200$//'