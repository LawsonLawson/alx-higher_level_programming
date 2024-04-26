#!/usr/bin/python3
"""
This script sends a GET request to a specified URL and prints the value of the
'X-Request-Id' header from the response.
"""

# Importing the 'sys' module for handling command-line arguments
import sys

# Importing the 'requests' module for handling HTTP requests
import requests

if __name__ == "__main__":
    # Send a GET request to the URL specified in the command-line arguments
    request = requests.get(sys.argv[1])

    # Print the value of the 'X-Request-Id' header from the response
    print(request.headers.get('X-Request-Id'))
