#!/bin/bash
# This script will trigger a session on youtube
# Only the audio will be transfered 
#
# Be sure to play fair
#
# #EXTINF:-1, YouTube Audio
# http://localhost/yt-play/?type=dl&src=6LEmDEZVa5g ...

sudo youtube-dl -f 140 --no-call-home -o '%(title)s.%(ext)s' $1
sudo mv *.m4a /mnt/SDCARD/YT