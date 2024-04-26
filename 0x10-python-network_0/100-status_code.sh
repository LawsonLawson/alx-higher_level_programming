#!/bin/bash
# This script prints the status code of the response.
curl -w "%{http_code}" -s -o /dev/null "$1"
