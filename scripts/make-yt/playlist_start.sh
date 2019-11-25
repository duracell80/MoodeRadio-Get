#!/bin/bash
# This script will trigger the actual playing of the YouTube_Play.m3u playlist
# The video is discarded, only audio plays (stream 140)
#
# Add to the playlist as ...
#
# #EXTINF:-1, YouTube Audio Start
# http://localhost/yt-play/?src=1

#sudo mpc update
#sudo mpc clear
#sudo mpc load /var/lib/mpd/playlists/YouTube_Play.m3u
#sudo mpc play