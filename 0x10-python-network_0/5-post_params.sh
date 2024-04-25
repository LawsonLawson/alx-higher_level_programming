#!/bin/bash
# This script sends a POST request to a specified URL with custom headers
curl -sX POST -d "emai=test@gmail.com&subject=I will always be here for PLD" "$1"
