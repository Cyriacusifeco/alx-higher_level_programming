#!/bin/bash
# Sends a GET request to the URL and displays the body of the response
curl -H "X-School-User-Id: 98" -sLX GET "$1"
