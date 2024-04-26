#!/usr/bin/python3
# Importing the module for handling URL requests
import urllib.request

# Open a connection to the specified URL
with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
    # Read the response body
    body = response.read()

    # Print a header for the response
    print('Body response:')

    # Print the type of the response of the response body
    print('\t- type: {}'.format(type(body)))

    # Print the content of the response body
    print('\t- content: {}'.format(body))

    # Print the content of the response body as UTF-8
    print('\t- utf8 content: {}'.format(body.decode('utf-8')))
