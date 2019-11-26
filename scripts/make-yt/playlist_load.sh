#!/bin/bash
# This script will trigger a session on youtube
# Lookup the meta data using only one pull
#
# Add to the playlist as ...
#
# #EXTINF:-1, YouTube Audio
# http://localhost/yt-play/?src=6LEmDEZVa5g ...

sudo youtube-dl -f 140 -j $1 > /var/www/yt-play/source.json
url=$(sudo python source_url.py)
title=$(sudo python source_title.py)

sudo echo "#EXTINF:-1, YouTube: "${title} >> /var/www/yt-play/yt.m3u
sudo echo ${url} >> /var/www/yt-play/yt.m3u
sudo cp -f /var/www/yt-play/yt.m3u /var/lib/mpd/playlists/YouTube_Play.m3u