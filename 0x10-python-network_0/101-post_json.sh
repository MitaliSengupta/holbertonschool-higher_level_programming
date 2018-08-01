#!/bin/bash
# script to send a Json POST req and display the response
curl -s "$1" -X POST -H "Content-Type: application/json" -d @"$2"
