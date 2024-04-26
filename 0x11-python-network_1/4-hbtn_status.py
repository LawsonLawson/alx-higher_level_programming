#!/usr/bin/python3
"""
This script uses the 'requests' module to fetch and display the body of a
response.
"""

# Importing the 'requests' module for handling HTTP requests
import requests

if __name__ == '__main__':
    # Send a GET request to the specified URL
    response = requests.get('https://alx-intranet.hbtn.io/status')

    # Print information about the response body
    print("Body response:")

    # Print the type of the response body
    print("\t- type: {}".format(type(response.text)))

    # Print the content of the response body
    print("\t- content: {}".format(response.text))
