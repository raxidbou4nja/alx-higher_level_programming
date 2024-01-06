#!/bin/bash
# Bash script that makes a POST request to a specified URL with a JSON payload
curl -sX POST -d "@$2" -H "Content-Type: application/json" "$1"
