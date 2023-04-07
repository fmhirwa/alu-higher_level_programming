#!/bin/bash
#Displays all HTTP methods acceptable on server
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
