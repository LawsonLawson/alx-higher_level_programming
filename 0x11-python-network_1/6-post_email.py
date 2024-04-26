#!/usr/bin/python3
"""
This script sends a POST request to a specified URL with a provided email
address.
"""

# For accessing command-line arguments and exiting the script
import sys

# For sending HTTP requests
import requests

if __name__ == "__main__":
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 3:
        print("Usage: ./post_email.py <URL> <email>")
        sys.exit(1)

    # Extract URL and email address from command-line arguments
    url = sys.argv[1]
    email = sys.argv[2]

    # Prepare the data payload for the POST request
    payload = {"email": email}

    # Send the POST request
    response = requests.post(url, data=payload)

    # Print the response body
    print(response.text)
