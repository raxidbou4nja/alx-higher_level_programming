#!/bin/bash
# Bash script that makes a POST request to a specified URL with a JSON payload
curl -sX POST -H "Content-Type: application/json" -d @"$2" "$1"
