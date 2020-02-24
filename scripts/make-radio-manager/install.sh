#!/bin/bash


# Create the organization in RADIO
sudo mkdir -p /var/lib/mpd/music/RADIO/_Stations/tags
sudo mkdir -p /var/lib/mpd/music/RADIO/_Stations/networks

# Copy scripts to localhost
sudo mkdir -p /var/www/radio/sources/rb
sudo mkdir -p /var/www/radio/sources/moode/scripts
sudo mkdir -p /var/www/radio/sources/moode/user/radio-images/thumbs
sudo cp -f ./radio/index.php /var/www/radio
sudo cp -f ./radio/sources/config.json /var/www/radio/sources
sudo cp -f ./radio/sources/repeater.js /var/www/radio/sources
sudo cp -rf ./radio/sources/moode /var/www/radio/sources
sudo cp -rf ./radio/sources/rb /var/www/radio/sources
sudo cp -f ./radio/sources/rb/*.m3u /var/lib/mpd/playlists
sudo cp -f ./www/rdo-config.php /var/www
sudo cp -f ./www/rdo-config-rb.php /var/www
sudo cp -f ./www/templates/rdo-config.html /var/www/templates
sudo cp -f ./www/templates/rdo-config-rb.html /var/www/templates
sudo cp -f ./radio/sources/stations.zip /var/www/radio/sources/
sudo cp -f ./radio/sources/stations.zip /var/lib/mpd/music/SDCARD

# Copy pre-installed radio tag logos to moode radio thumbs


# Permissions
sudo chmod 777 /var/lib/mpd/playlists/Radio_Play.m3u
sudo chmod 777 /var/www/radio/index.php
sudo chmod 777 /var/www/radio/sources/moode
sudo chmod 777 /var/www/radio/sources/moode/scripts
sudo chmod 777 /var/www/radio/sources/moode/user
sudo chmod 777 /var/www/radio/sources/moode/user/radio-logos
sudo chmod 777 /var/www/radio/sources/moode/user/radio-logos/thumbs
sudo chmod 777 /var/www/radio/sources/config.json
sudo chmod 777 /var/www/radio/sources/rb/tags.json
sudo chmod 755 /var/www/radio/sources/rb/*.py
sudo chmod 755 /var/www/radio/sources/moode/*.py
sudo chmod 755 /var/www/rdo-config.php
sudo chmod 755 /var/www/rdo-config-rb.php
sudo chmod 755 /var/www/templates/rdo-config.html
sudo chmod 755 /var/www/templates/rdo-config-usr.html
