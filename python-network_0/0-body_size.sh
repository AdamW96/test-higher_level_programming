#!/bin/bash
# This script takes a URL, sends a request to it, and displays the size of the response body in bytes
curl -s "$1" | wc -c