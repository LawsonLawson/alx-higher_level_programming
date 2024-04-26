#!/usr/bin/python3
"""
This script uses the GitHub API to display a GitHub ID based on given
credentials.
"""

# Import the sys module for accessing command-line arguments
import sys

# Import the requests module for making HTTP requests
import requests

# Import HTTPBasicAuth for Basic Authentication
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 3:
        print("Usage: ./my_github.py <GitHub username> <GitHub password>")
        sys.exit(1)

    # Create Basic Authentication object with provided credentials
    auth = HTTPBasicAuth(sys.argv[1], sys.argv[2])

    # Send GET request to GitHub API to retrieve user information
    response = requests.get("https://api.github.com/user", auth=auth)

    # Print the GitHub user ID
    print(response.json().get("id"))
