#!/bin/bash



# Copy scripts to localhost
sudo mkdir -p /var/www/radio/sources/rb
sudo cp -f ./radio/index.php /var/www/radio
sudo cp -f ./radio/sources/config.json /var/www/radio/sources
sudo cp -rf ./radio/sources/rb /var/www/radio/sources

# Copy new admin config UI but don't override users lib-config
sudo cp -f ./www/templates/rdo-config.html /var/www/templates
sudo cp -f ./www/rdo-config.php /var/www

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
sudo cp -f ./YouTube_Play.jpg /var/www/images/radio-logos/thumbs/example-streaming.jpg
#sudo cp -f ./yt-dl.m3u /var/lib/mpd/music/RADIO/_YouTube/example-downloading.m3u




# Permissions
sudo chmod 755 ./uninstall.sh
#sudo cp -f ./uninstall.sh /var/www/yt-play/uninstall.sh

sudo chmod 755 /var/www/yt-play/*.php
sudo chmod 755 /var/www/yt-play/*.sh
sudo chmod 777 /var/www/yt-play/*.m3u
sudo chmod 777 /var/www/yt-play/*.py
sudo chmod 777 /var/www/yt-play/*.json




mpc update







