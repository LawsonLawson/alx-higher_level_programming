#!/bin/bash
# This script takes in a URL, sends a request to the URL and displays the size
curl -s "$1" | wc -c
