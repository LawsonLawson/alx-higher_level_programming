#!/bin/bash
# This script sends a GET request to a specified URL with a custom header
curl -sH "X-School-User-Id: 98" "$1"
