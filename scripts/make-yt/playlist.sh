#!/bin/bash
# Find the audio stream using having replaced the video ID with your target
# youtube-dl --list-formats https://m.youtube.com/watch?v=6LEmDEZVa5g 
#
# Then run ...
# ./playlist 140 https://m.youtube.com/watch?v=6LEmDEZVa5g

sudo youtube-dl -f $1 -g $2 > source.txt
echo "#EXTINF:-1, YouTube Audio $2" > source-header.txt
cat source-header.txt >> yt.m3u
cat source.txt >> yt.m3u
sudo cp yt.m3u /var/lib/mpd/playlists/YouTube_Audio.m3u
