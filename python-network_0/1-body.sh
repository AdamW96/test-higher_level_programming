#!/bin/bash
# This script sends a GET request to a URL and displays the body only for 200 status code responses
curl -s -L -o /tmp/body -w "%{http_code}" "$1" | grep -q "200" && cat /tmp/body