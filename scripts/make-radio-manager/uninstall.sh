#!/bin/bash


# Destroy the organization in RADIO and MPD Playlists
sudo rm -rf /var/lib/mpd/music/RADIO/_Stations
sudo rm -rf /var/lib/mpd/playlists/Radio_Play.m3u

# Destroy scripts from localhost
sudo rm -rf /var/www/radio
sudo rm -rf /var/www/rdo-config.php
sudo rm -rf /var/www/rdo-config-rb.php
sudo rm -rf /var/www/templates/rdo-config.html
sudo rm -rf /var/www/templates/rdo-config-rb.html


# Remove moode radio logos
sudo rm -rf /var/www/images/radio-logos/bbc.jpg
sudo rm -rf /var/www/images/radio-logos/npr.jpg
sudo rm -rf /var/www/images/radio-logos/dashradio.jpg
sudo rm -rf /var/www/images/radio-logos/thumbs/bbc.jpg
sudo rm -rf /var/www/images/radio-logos/thumbs/npr.jpg
sudo rm -rf /www/images/radio-logos/thumbs/dashradio.jpg

# Remove podcast API for RADIO ... sad day
sudo rm -rf /var/www/radio/sources/pod
sudo rm -rf /var/lib/mpd/music/RADIO/_Podcasts
sudo rm -rf /var/lib/mpd/playlists/podcast_*

mpc update