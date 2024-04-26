#!/usr/bin/python3
"""
This script sends a POST request to http://0.0.0.0:5000/search_user with
a given letter.
"""

# Import the sys module for accessing command-line arguments
import sys

# Import the requests module for making HTTP requests
import requests


if __name__ == "__main__":
    # Check if a letter is provided in the command-line arguments
    if len(sys.argv) == 1:
        letter = ""
    else:
        letter = sys.argv[1]

    # Prepare the payload for the POST request
    payload = {"q": letter}

    # Send the POST request to the specified URL
    response = requests.post("http://0.0.0.0:5000/search_user", data=payload)

    try:
        # Attempt to parse the response as JSON
        json_response = response.json()

        # Check if the response is empty
        if json_response == {}:
            print("No result")
        else:
            # Print the ID and name from the response
            print("[{}] {}".format(json_response.get("id"),
                  json_response.get("name")))
    except ValueError:
        # Handle case where the response is not valid JSON
        print("Not a valid JSON")
