#!/bin/bash
# This script will clear the YouTube_Audio.m3u playlist
# Do this with ...
#
# #EXTINF:-1, YouTube Audio
# http://localhost/yt-play/?type=stream&src=0


sudo echo "#EXTM3U" > /var/www/yt-play/yt.m3u
sudo cp -f /var/www/yt-play/yt.m3u /var/lib/mpd/playlists/YouTube_Play.m3u