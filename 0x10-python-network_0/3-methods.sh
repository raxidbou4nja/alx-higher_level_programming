#!/bin/bash
# Use curl to display all HTTP methods the server will accept
curl -sI -X OPTIONS "$1" | grep "Allow:" | cut -d' ' -f2-
