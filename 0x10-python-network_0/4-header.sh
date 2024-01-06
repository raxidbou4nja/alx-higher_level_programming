#!/bin/bash
# Use curl to send a GET request with a custom header and display the body of the response
curl -s "$1" -X GET -H "X-School-User-Id: 98"
