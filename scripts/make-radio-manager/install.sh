#!/bin/bash


# Create the organization in RADIO
sudo mkdir -p /var/lib/mpd/music/RADIO/_Stations/tags
sudo mkdir -p /var/lib/mpd/music/RADIO/_Stations/networks

# Copy scripts to localhost
sudo mkdir -p /var/www/radio/sources/rb
sudo mkdir -p /var/www/radio/sources/moode
sudo cp -f ./radio/index.php /var/www/radio
sudo cp -f ./radio/sources/config.json /var/www/radio/sources
sudo cp -rf ./radio/sources/rb /var/www/radio/sources
sudo cp -f ./radio/sources/rb/*.m3u /var/lib/mpd/playlists
sudo cp -f ./www/rdo-config.php /var/www
sudo cp -f ./www/templates/rdo-config.html /var/www/templates

# Permissions
sudo chmod 777 /var/lib/mpd/playlists/Radio_Play.m3u
sudo chmod 777 /var/www/radio/index.php
sudo chmod 777 /var/www/radio/sources/moode
sudo chmod 777 /var/www/radio/sources/config.json
sudo chmod 777 /var/www/radio/sources/rb/tags.json
sudo chmod 755 /var/www/radio/sources/rb/*.py
sudo chmod 755 /var/www/rdo-config.php
sudo chmod 755 /var/www/templates/rdo-config.html
