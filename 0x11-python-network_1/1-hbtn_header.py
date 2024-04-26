#!/usr/bin/python3
"""
This script displays the value of the X-Request-Id header variable from a
response to a given URL.
"""

# Importing sys in order to get access to command line arguments
import sys

# Importing the module for handling URL requests
import urllib.request

if __name__ == '__main__':
    # Extract the URL from the command-line arguments
    url = sys.argv[1]

    # Create a request object for the specified URL
    request = urllib.request.Request(url)

    # Open a connection to the URL and send the request
    with urllib.request.urlopen(request) as response:

        # Retrive and print the value of the X-Request-Id header, if present
        x_request_id = dict(response.headers).get('X-Request-Id')
        print(f'{x_request_id}')
