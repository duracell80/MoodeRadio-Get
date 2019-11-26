#!/bin/bash
# This script will trigger a session on youtube
# Lookup the meta data using only one pull
#
# http://localhost/yt-play/?type=info&src=6LEmDEZVa5g ...

sudo youtube-dl -f 140 -j $1 > /var/www/yt-play/source.json
output=$(cat /var/www/yt-play/source.json)
echo ${output}