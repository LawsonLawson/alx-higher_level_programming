#!/usr/bin/python3
"""
This script sends a POST request to a given URL with a given email and displays
the body of the response.
"""

# For the sake command line arguments, importing sys
import sys

# Importing module for parsing URLs
import urllib.parse

# Importing module for handling requests
import urllib.request

if __name__ == '__main__':
    # Extract the URL from the command-line arguments
    url = sys.argv[1]

    # Extract the email from the command line arguments
    email = sys.argv[2]

    # Encode the email as a dictionary
    value = {'email': email}

    # Encode the data for the POST request
    data = urllib.parse.urlencode(value).encode('ascii')

    # Create a request object for the specified URL and date
    request = urllib.request.Request(url, data)

    # Open a connection to the URL and send the request
    with urllib.request.urlopen(request) as response:
        # Print the body of the response
        print(response.read().decode('utf-8'))
