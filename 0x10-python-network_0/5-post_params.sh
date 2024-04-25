#!/bin/bash
# This script sends a POST request to a specified URL with custom headers
curl -sX POST -d "$1" "emai=test@gmail.com&subject=I will always be here for PLD"
