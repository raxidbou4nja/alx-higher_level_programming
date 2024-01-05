#!/bin/bash

# Use curl to send a request and display the size of the response body in bytes
curl -sI "$1" | awk '/Content-Length/ {print $2}'
