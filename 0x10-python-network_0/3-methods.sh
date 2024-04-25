#!/bin/bash
# This script displays the allowed HTTP methods for a specified URL
curl -siIX OPTIONS "$1" | grep "Allow" | cut -d " " -f2-
