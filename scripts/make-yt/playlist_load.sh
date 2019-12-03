#!/bin/bash
# This script will trigger a session on youtube
# Lookup the meta data using only one pull
#
# Add to the playlist as ...
#
# #EXTINF:-1, YouTube Audio
# http://localhost/yt-play/?src=6LEmDEZVa5g ...
# Proxy 192.241.187.83:31650


sudo youtube-dl -f 249 -U --no-warnings --skip-download -i --sleep-interval 30 --proxy socks5://192.241.187.83:31650 --force-ipv4 -j $1 > /var/www/yt-play/source.json
#id=$(sudo python source_id.py)
url=$(sudo python source_url.py)
duration=$(sudo python source_duration.py)
title=$(sudo python source_title.py)
#image=$(sudo python source_image.py)


sudo echo "#EXTINF:"${duration}", YouTube: "${title} >> /var/www/yt-play/yt.m3u
sudo echo ${url} >> /var/www/yt-play/yt.m3u
sudo cp -f /var/www/yt-play/yt.m3u /var/lib/mpd/playlists/YouTube_Play.m3u