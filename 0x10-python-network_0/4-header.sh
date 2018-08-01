#!/bin/bash
# script to send GET request with header var X-HolbertonSchool-User-Id val 98
curl -s "$1" -X GET -H "X-HolbertonSchool-User-Id:98"
