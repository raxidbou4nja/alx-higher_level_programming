#!/bin/bash
# Use curl to send a GET request with a custom header and display the body of the response
curl -sH "X-School-User-Id: 98" "$1" && echo ""
