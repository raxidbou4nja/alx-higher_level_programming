#!/bin/bash
# Use curl to display all HTTP methods the server will accept
curl -si "$1" | awk -F ": " '/Allow/ {print $2}'
