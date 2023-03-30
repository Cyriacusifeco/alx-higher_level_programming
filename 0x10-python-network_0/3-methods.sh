#!/bin/bash
# Displays all HTTP methods the server will accept
curl -sI "$1" -X OPTIONS | grep -i Allow: | cut -d " " -f2-
