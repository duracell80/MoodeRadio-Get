#!/bin/bash
# This script will trigger a session on youtube
# Only the audio will be transfered 
#
# Be sure to play fair
#
# #EXTINF:-1, YouTube Audio
# http://localhost/yt-play/?type=download&src=6LEmDEZVa5g ...

sudo cd /mnt/SDCARD/YT/
sudo youtube-dl -f 249 --no-call-home -o '%(title)s-%(id)s.%(ext)s' $1