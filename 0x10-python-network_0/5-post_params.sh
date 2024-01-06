#!/bin/bash
# Use curl to send a POST request with specified parameters and display the body of the response
curl -s "$1" -X POST -d "email=test@gmail.com&subject=I will always be here for PLD"
