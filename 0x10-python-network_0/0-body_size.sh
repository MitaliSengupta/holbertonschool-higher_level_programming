#!/bin/bash
# displaying size of the body of response after curl
curl -sI "$1" | grep "Content-Length" | cut -d' ' -f 2
