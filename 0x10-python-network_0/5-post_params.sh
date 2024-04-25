#!/bin/bash
# This script sends a POST request to a specified URL with custom headers
curl -sX POST "$1" -H "email: test@gmail.com" -H "subject: I will always be here for PLD"
