#!/bin/bash
# This script will trigger a session on youtube
# Only the audio will be transfered 
#
# Add to the playlist as ...
#
# #EXTINF:-1, YouTube Audio
# http://localhost/yt-play/?src=6LEmDEZVa5g ...

sudo youtube-dl -f 140 -g $1 > source.txt
title=$(sudo youtube-dl -e $1)

sudo echo "#EXTINF:-1, YouTube: "${title} >> /var/www/yt-play/yt.m3u
sudo cat source.txt >> /var/www/yt-play/yt.m3u
sudo cp -f /var/www/yt-play/yt.m3u /var/lib/mpd/playlists/YouTube_Play.m3u