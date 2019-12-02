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

# DOWNLOAD (video id)
# #EXTINF:-1, YouTube Audio
# http://localhost/yt-play/?dl=true&src=6LEmDEZVa5g


# The following commands set everything up

#sudo apt-get install vlc-bin
sudo apt-get install python-pip
sudo pip install --upgrade youtube_dl
#sudo apt-get install mps-youtube



# Copy helper scripts to localhost
sudo mkdir -p /var/www/yt-play
sudo mkdir -p /var/lib/mpd/music/RADIO/_YouTube
sudo cp -f ./index.php /var/www/yt-play
sudo cp -f ./source.json /var/www/yt-play
sudo cp -f ./sourcelist.json /var/www/yt-play
sudo cp -f ./sourcelist.py /var/www/yt-play
sudo cp -f ./source_title.py /var/www/yt-play
sudo cp -f ./source_url.py /var/www/yt-play
sudo cp -f ./source_duration.py /var/www/yt-play
sudo cp -f ./playlist_clear.sh /var/www/yt-play
sudo cp -f ./playlist_load.sh /var/www/yt-play
sudo cp -f ./playlist_loadlist.sh /var/www/yt-play
sudo cp -f ./playlist_start.sh /var/www/yt-play
sudo cp -f ./playlist_regen.sh /var/www/yt-play
sudo cp -f ./playlist_dl.sh /var/www/yt-play
sudo cp -f ./yt-info.sh /var/www/yt-play

# Downloads discouraged, but if wanted create folder, copy helper to localhost
sudo mkdir -p /mnt/SDCARD/YT
sudo cp -f ./yt-dl.sh /var/www/yt-play


# Copy Base Playlists
sudo cp -f ./yt-init.m3u /var/lib/mpd/playlists/YouTube_Load.m3u
sudo cp -f ./yt.m3u /var/lib/mpd/playlists/YouTube_Play.m3u
sudo cp -f ./yt-init.m3u /var/www/yt-play/yt-init.m3u
sudo cp -f ./yt.m3u /var/www/yt-play/yt.m3u
sudo cp -f ./yt.m3u /var/www/yt-play/yt-list.m3u
sudo cp -rf ./_YouTube/* /var/lib/mpd/music/RADIO/_YouTube
sudo cp -f ./yt-init.m3u /var/lib/mpd/music/RADIO/_YouTube/example-streaming.m3u
sudo cp -f ./YouTube_Play.jpg /var/www/images/radio-logos/thumbs/yt-example.jpg
sudo cp -f ./YouTube_Play.jpg /var/www/images/radio-logos/thumbs/yt-example-list.jpg
sudo cp -f ./YouTube_Play.jpg /var/www/images/radio-logos/thumbs/streaming-example.jpg
#sudo cp -f ./yt-dl.m3u /var/lib/mpd/music/RADIO/_YouTube/example-downloading.m3u

mpc update


# Permissions
sudo chmod 755 ./uninstall.sh
#sudo cp -f ./uninstall.sh /var/www/yt-play/uninstall.sh

sudo chmod 755 /var/www/yt-play/*.php
sudo chmod 755 /var/www/yt-play/*.sh
sudo chmod 777 /var/www/yt-play/*.m3u
sudo chmod 777 /var/www/yt-play/*.py
sudo chmod 777 /var/www/yt-play/*.json












