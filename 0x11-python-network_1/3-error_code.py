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
    try:
        # Extract the URL from the command-line arguments
        url = sys.argv[1]

        # Open a connection to the URL
        with urllib.request.urlopen(url) as response:
            # Read and print the body of the response
            print(response.read().decode('utf-8'))
    except urllib.error.HTTPError as error:
        # Print the error code if an HTTP error occurs
        print('HTTP Error code: {}'.format(error.code))
