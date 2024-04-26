#!/bin/bash
# This script sends a POST request to a specified URL with custom headers
curl -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
