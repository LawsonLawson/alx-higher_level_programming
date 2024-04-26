#!/usr/bin/python3
"""
This script handles HTTP errors by printing the errore code.
"""


# For the sake command line arguments, importing sys
import sys

# Importing module for errors
import urllib.error

# Importing module for handling requests
import urllib.request


if __name__ == '__main__':
    # Extract the URL from the command-line arguments
    url = sys.argv[1]

    request = urllib.request.Request(url)

    try:

        # Open a connection to the URL
        with urllib.request.urlopen(request) as response:

            # Read and print the body of the response
            print(response.read().decode('ascii'))

    except urllib.error.HTTPError as error:
        # Print the error code if an HTTP error occurs
        print('Error code: {}'.format(error.code))
