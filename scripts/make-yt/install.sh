#!/bin/bash
# This script package provides Moode a PHP file on localhost that builds a dynamic playlist that streams 
# audio from YouTube. It uses youtube-dl to select stream 140 to provide .m4a files.
#
#
# IMPORTANT: The links generated expire usually after 6 hours.
# IMPORTANT: When the links expire re-run the YouTube_Load.m3u playlist.
#
# Create your YouTube_Load.m3u file with the following commands
# The loading playlist with the localhost helper can be located in the RADIO folder too

# CLEAR
# #EXTINF:-1, YouTube Audio
# http://localhost/yt-play/?src=0

# LOAD (video id)
# #EXTINF:-1, YouTube Audio
# http://localhost/yt-play/?src=6LEmDEZVa5g


# The following commands set everything up


sudo apt-get install python-pip
sudo pip install --upgrade youtube_dl
#sudo apt-get install mps-youtube

sudo mkdir -p /var/lib/mpd/music/SDCARD/YT
sudo mkdir -p /var/www/yt-play
sudo cp -f ./index.php /var/www/yt-play
sudo cp -f ./yt-init.m3u /var/lib/mpd/playlists/YouTube_Load.m3u
sudo cp -f ./yt.m3u /var/lib/mpd/playlists/YouTube_Play.m3u
sudo cp -f ./yt.m3u /var/www/yt-play/yt.m3u
sudo cp -f ./source.txt /var/www/yt-play
sudo cp -f ./playlist_clear.sh /var/www/yt-play
sudo cp -f ./playlist_load.sh /var/www/yt-play
sudo cp -f ./playlist_start.sh /var/www/yt-play