#!/bin/bash
# This script will trigger a session on youtube
# Only the audio will be transfered 
#
# Be sure to play fai
#
# #EXTINF:-1, YouTube Audio
# http://localhost/yt-play/?dl=1&src=6LEmDEZVa5g ...

sudo cd /mnt/SDCARD/YT/
sudo sudo youtube-dl -f 140 --no-call-home -o '%(title)s.%(ext)s' $1