#!/bin/bash
#URL input | Request send to  URL | Displays body size
curl -s "$1" | wc -c
