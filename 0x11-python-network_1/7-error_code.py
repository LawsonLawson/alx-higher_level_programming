#!/usr/bin/python3
"""
This script sends a GET request to a specified URL and displays the response
body.
"""

# Import the sys module for accessing command-line arguments
import sys

# Import the requests module for making HTTP requests
import requests

if __name__ == "__main__":
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 2:
        print("Usage: ./error_code.py <URL>")
        sys.exit(1)

    # Extract URL from command-line arguments
    url = sys.argv[1]

    # Send the GET request
    response = requests.get(url)

    # Check for HTTP errors
    if response.status_code >= 400:
        print("Error code: {}".format(response.status_code))
    else:
        print(response.text)
