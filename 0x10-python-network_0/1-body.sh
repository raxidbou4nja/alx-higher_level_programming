#!/bin/bash
# Use curl to send a GET request and display the body of the response for a 200 status code
if [ "$(curl -sLI "$1" -X GET | grep "200 OK" | cut -d' ' -f2)" = '200' ]; then
    curl -sL "$1"
fi
echo ""
