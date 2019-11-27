#!/bin/bash
# This script package provides Moode a PHP file on localhost that builds a dynamic playlist that streams 
# audio from YouTube. It uses youtube-dl to select stream 140 to provide .m4a files.
#
#
# The following commands break everything down and pack it away like a dedicated roadie

#sudo pip -y uninstall youtube_dl
#sudo apt-get -y remove mps-youtube
#sudo apt-get -y remove vlc-bin


# Wreck the stage
sudo rm -rf /var/www/yt-play

# Wipe the downloads
#sudo rm -rf /mnt/SDCARD/YT


# Remove Base Playlists
sudo rm -rf /var/lib/mpd/playlists/YouTube_Load.m3u
sudo rm -rf /var/lib/mpd/playlists/YouTube_Play.m3u
sudo rm -rf /var/lib/mpd/music/RADIO/_YouTube/asmr/example.m3u
sudo rm -rf /var/lib/mpd/music/RADIO/_YouTube/mahogany/example.m3u
sudo rm -rf /var/lib/mpd/music/RADIO/_YouTube/example-downloading.m3u
sudo rm -rf /var/lib/mpd/music/RADIO/_YouTube/example-streaming.m3u


mpc update